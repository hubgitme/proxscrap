#!/usr/bin/env python3
"""
Send the top N fastest MTProto proxies from proxy.txt to a Telegram channel.

Reads the proxy list produced by main.py (proxy.txt), re-checks each proxy
with a TCP connect (measuring latency), picks the fastest ones that were
not sent recently, and posts ONE message with one "connect" inline button
per proxy.

Required environment variables (set as GitHub Secrets, never hardcode):
  TELEGRAM_BOT_TOKEN   Bot token from @BotFather
  TELEGRAM_CHAT_ID     Channel id: @YourChannel  or  -100xxxxxxxxxx

Optional:
  TOP_N                How many proxies per post (default: 4)
  EXCLUDE_HOURS        Don't resend a proxy sent in the last N hours (default: 6)
  CHECK_TIMEOUT        TCP connect timeout in seconds (default: 3)
  CHECK_WORKERS        Parallel check workers (default: 50)
  PROXY_FILE           Path to proxy.txt (default: ../proxy.txt next to this file)
  HISTORY_FILE         Path to last_sent.json (default: last_sent.json next to this file)
  CHANNEL_FOOTER       Optional footer line, e.g. "@YourChannel"
  DRY_RUN              If "1": print the payload, do not send
  SKIP_CHECK           If "1": skip network checks (for tests), keep file order
"""

import html
import json
import logging
import os
import re
import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from urllib.parse import parse_qs, urlparse

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PROXY_PATH = os.path.normpath(os.path.join(BASE_DIR, "../proxy.txt"))
DEFAULT_HISTORY_PATH = os.path.join(BASE_DIR, "last_sent.json")

TOP_N = int(os.environ.get("TOP_N", "5"))
EXCLUDE_HOURS = float(os.environ.get("EXCLUDE_HOURS", "6"))
CHECK_TIMEOUT = float(os.environ.get("CHECK_TIMEOUT", "3"))
CHECK_WORKERS = int(os.environ.get("CHECK_WORKERS", "50"))
PROXY_FILE = os.environ.get("PROXY_FILE", DEFAULT_PROXY_PATH)
HISTORY_FILE = os.environ.get("HISTORY_FILE", DEFAULT_HISTORY_PATH)
CHANNEL_FOOTER = os.environ.get("CHANNEL_FOOTER", "").strip()
DRY_RUN = os.environ.get("DRY_RUN", "") == "1"
SKIP_CHECK = os.environ.get("SKIP_CHECK", "") == "1"

SERVER_RE = re.compile(r"[A-Za-z0-9._-]+")
SECRET_RE = re.compile(r"[A-Za-z0-9_\-+/=]+")


def parse_proxy_link(link):
    """Parse tg://proxy or https://t.me/proxy link -> (server, port, secret) or None."""
    link = html.unescape((link or "").strip())
    if not link.startswith(("tg://proxy", "https://t.me/proxy", "http://t.me/proxy")):
        return None
    try:
        # keep '+' in base64 secrets (parse_qs would turn it into a space)
        query = parse_qs(urlparse(link).query.replace("+", "%2B"))
        server = query["server"][0].strip().rstrip(".")
        port = int(query["port"][0])
        secret = query["secret"][0].strip()
    except (KeyError, IndexError, ValueError):
        return None
    if not (0 < port < 65536):
        return None
    if not SERVER_RE.fullmatch(server) or not SECRET_RE.fullmatch(secret):
        return None
    return server, port, secret


def make_link(server, port, secret):
    return f"https://t.me/proxy?server={server}&port={port}&secret={secret}"


def check_latency_ms(server, port, timeout=CHECK_TIMEOUT):
    """Return TCP connect latency in ms, or None if unreachable."""
    start = time.perf_counter()
    try:
        with socket.create_connection((server, int(port)), timeout=timeout):
            return int((time.perf_counter() - start) * 1000)
    except (OSError, UnicodeError, ValueError):
        return None


def load_proxies(path):
    """Load and de-duplicate proxies from proxy.txt. Returns [(server, port, secret)]."""
    proxies = []
    seen = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            parsed = parse_proxy_link(line)
            if not parsed:
                continue
            key = (parsed[0].lower(), parsed[1], parsed[2])
            if key in seen:
                continue
            seen.add(key)
            proxies.append(parsed)
    return proxies


def load_history(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (OSError, ValueError):
        return []


def save_history(path, history):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(history[-100:], f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def recently_sent_links(history, now, exclude_hours):
    cutoff = now - timedelta(hours=exclude_hours)
    links = set()
    for item in history:
        try:
            sent_at = datetime.fromisoformat(item["sent_at"].replace("Z", "+00:00"))
        except (KeyError, ValueError, AttributeError):
            continue
        if sent_at >= cutoff:
            links.add(item.get("link", ""))
    return links


def rank_proxies(proxies):
    """Check all proxies in parallel. Returns [(latency_ms, server, port, secret)] sorted fastest first."""
    if SKIP_CHECK:
        # Test mode: keep file order, fake increasing latency
        return [(i + 1, s, p, sec) for i, (s, p, sec) in enumerate(proxies)]
    ranked = []
    with ThreadPoolExecutor(max_workers=CHECK_WORKERS) as executor:
        futures = {
            executor.submit(check_latency_ms, s, p): (s, p, sec) for s, p, sec in proxies
        }
        for future in as_completed(futures):
            server, port, secret = futures[future]
            try:
                latency = future.result()
            except Exception as e:  # noqa: BLE001 - one bad proxy must not kill the run
                logging.warning("Check failed for %s:%s: %s", server, port, e)
                continue
            if latency is not None:
                ranked.append((latency, server, port, secret))
    ranked.sort(key=lambda x: x[0])
    return ranked


def pick_top(ranked, top_n, exclude_links):
    """Pick fastest proxies, skipping recently sent ones and duplicate servers."""
    picked = []
    used_servers = set()
    for latency, server, port, secret in ranked:
        link = make_link(server, port, secret)
        if link in exclude_links:
            continue
        if server.lower() in used_servers:
            continue
        used_servers.add(server.lower())
        picked.append((latency, server, port, secret))
        if len(picked) >= top_n:
            break
    if len(picked) < top_n:
        # Not enough fresh ones: fill with the fastest regardless of history
        for latency, server, port, secret in ranked:
            if server.lower() in used_servers:
                continue
            used_servers.add(server.lower())
            picked.append((latency, server, port, secret))
            if len(picked) >= top_n:
                break
    return picked


def tehran_now_str(now_utc):
    """Human-readable Tehran time; Jalali date when jdatetime is available."""
    try:
        from zoneinfo import ZoneInfo

        tehran = now_utc.astimezone(ZoneInfo("Asia/Tehran"))
    except Exception:  # noqa: BLE001
        tehran = now_utc + timedelta(hours=3, minutes=30)
    try:
        import jdatetime

        jalali = jdatetime.datetime.fromgregorian(datetime=tehran)
        return jalali.strftime("%Y/%m/%d - %H:%M")
    except Exception:  # noqa: BLE001
        return tehran.strftime("%Y-%m-%d %H:%M")


def build_message(top, now_utc):
    """Build (text, reply_markup) for one channel post with connect buttons."""
    lines = [
        "🔥 <b>۴ پروکسی برتر</b>",
        "━━━━━━━━━━━━━━",
        f"⏰ <i>{html.escape(tehran_now_str(now_utc))}</i>",
        "",
    ]
    buttons = []
    for i, (latency, server, port, secret) in enumerate(top, 1):
        link = make_link(server, port, secret)
        # In-text hyperlink with a text label (no raw IP shown), same link as the button
        lines.append(
            f'{i}️⃣ <a href="{html.escape(link, quote=True)}">اتصال به آدرس {i}</a>'
            f" — ⚡ {latency}ms"
        )
        buttons.append(
            [{"text": f"🔗 اتصال به پروکسی {i} ({latency}ms)", "url": link}]
        )
    lines.append("")
    lines.append("━━━━━━━━━━━━━━")
    lines.append("👇 برای اتصال روی لینک‌ها یا دکمه‌ها بزنید")
    if CHANNEL_FOOTER:
        lines.append(f"📢 {html.escape(CHANNEL_FOOTER)}")
    return "\n".join(lines), {"inline_keyboard": buttons}


def send_telegram(token, chat_id, text, reply_markup):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    resp = requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
            "reply_markup": reply_markup,
        },
        timeout=30,
    )
    data = resp.json() if resp.headers.get("content-type", "").startswith("application/json") else {}
    if resp.status_code != 200 or not data.get("ok"):
        # Never log the token; Telegram's description is safe to show
        raise RuntimeError(f"Telegram API error {resp.status_code}: {data.get('description', resp.text[:200])}")
    return data["result"]["message_id"]


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not DRY_RUN and (not token or not chat_id):
        logging.error("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set (GitHub Secrets).")
        return 2

    proxies = load_proxies(PROXY_FILE)
    logging.info("Loaded %d proxies from %s", len(proxies), PROXY_FILE)
    if not proxies:
        logging.error("No valid proxies in %s - nothing to send.", PROXY_FILE)
        return 1

    ranked = rank_proxies(proxies)
    logging.info("%d of %d proxies are online", len(ranked), len(proxies))
    if not ranked:
        logging.error("No online proxies - skipping this hour (no post sent).")
        return 1

    now = datetime.now(timezone.utc)
    history = load_history(HISTORY_FILE)
    exclude = recently_sent_links(history, now, EXCLUDE_HOURS)
    top = pick_top(ranked, TOP_N, exclude)
    logging.info("Top %d: %s", len(top), [(f"{s}:{p}", f"{ms}ms") for ms, s, p, _ in top])

    text, reply_markup = build_message(top, now)

    if DRY_RUN:
        print("--- DRY RUN (nothing sent) ---")
        print(text)
        print(json.dumps(reply_markup, ensure_ascii=False, indent=1))
        return 0

    message_id = send_telegram(token, chat_id, text, reply_markup)
    logging.info("Sent message %s to %s", message_id, chat_id)

    for _latency, server, port, secret in top:
        history.append({"link": make_link(server, port, secret), "sent_at": now.isoformat()})
    save_history(HISTORY_FILE, history)
    return 0


if __name__ == "__main__":
    sys.exit(main())
