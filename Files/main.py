import requests
from bs4 import BeautifulSoup
import re
import random
import time
import logging
from datetime import datetime
import pytz
import jdatetime
import unicodedata
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import sys
import html
from urllib.parse import urlparse, parse_qs

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PROXY_PATH = os.path.normpath(os.path.join(BASE_DIR, '../proxy.txt'))
DEFAULT_README_PATH = os.path.normpath(os.path.join(BASE_DIR, '../README.md'))

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

TEXT_URLS = [
    "https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt",
    "https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt",
    "https://itsyebekhe.github.io/MTProtoNexus/extracted_proxies.json",
    "https://raw.githubusercontent.com/darkvibez456/mtproto-proxy-auto/refs/heads/main/proxies.txt",
]

TELEGRAM_URLS = [
    "https://t.me/s/webproxy",
    "https://t.me/s/iporoto",
    "https://t.me/s/HiProxy",
    "https://t.me/s/iproxy",
    "https://t.me/s/iRoProxy",
    "https://t.me/s/proxyforopeta",
    "https://t.me/s/IRN_Proxy",
    "https://t.me/s/MProxy_ir",
    "https://t.me/s/ProxyHagh",
    "https://t.me/s/PyroProxy",
    "https://t.me/s/ProxyMTProto",
    "https://t.me/s/MTPro_XYZ",
    "https://t.me/s/vpns",
    "https://t.me/s/mtmvpn",
    "https://t.me/s/asr_proxy",
    "https://t.me/s/proxyskyy",
]

LINK_RE = re.compile(r"(?:tg://proxy|https?://t\.me/proxy)\?[^\s<>\"'`|)]+")
HEX_RE = re.compile(r"^[0-9a-fA-F]+$")
CHECK_WORKERS = 100
CHECK_TIMEOUT = 3


def clean_line(line):
    line = line.strip().replace('\r', '').replace('\n', '')
    line = ''.join(c for c in line if unicodedata.category(c)[0] != 'C')
    return line


def parse_proxy_link(link):
    """Parse a proxy link (any parameter order, tg:// or t.me) -> (server, port, secret) or None."""
    link = html.unescape(clean_line(link))
    if not link.startswith(('tg://proxy', 'https://t.me/proxy', 'http://t.me/proxy')):
        return None
    try:
        # keep '+' characters of base64 secrets (parse_qs would turn them into spaces)
        query = parse_qs(urlparse(link).query.replace('+', '%2B'))
        server = query['server'][0].strip().rstrip('.')
        port = int(query['port'][0])
        secret = query['secret'][0].strip()
    except (KeyError, IndexError, ValueError):
        return None
    if not (0 < port < 65536):
        return None
    # allow only safe characters (the values end up in README markdown and web pages)
    if not re.fullmatch(r'[A-Za-z0-9._-]+', server):
        return None
    if not re.fullmatch(r'[A-Za-z0-9_\-+/=]+', secret):
        return None
    return server, port, secret


def make_link(server, port, secret):
    return f"https://t.me/proxy?server={server}&port={port}&secret={secret}"


def check_proxy_status(server, port, timeout=CHECK_TIMEOUT):
    """Return True if a TCP connection to the proxy can be opened."""
    try:
        with socket.create_connection((server, int(port)), timeout=timeout):
            return True
    except (OSError, UnicodeError, ValueError):
        return False


def fetch_candidates_from_text_urls(urls):
    """Download proxy lists (text or JSON). Returns unchecked (server, port, secret) tuples."""
    candidates = []
    for url in urls:
        found = []
        try:
            logging.info(f"Fetching proxies from {url}")
            response = requests.get(url, headers={'User-Agent': get_random_user_agent()}, timeout=15)
            response.raise_for_status()

            if url.endswith('.json'):
                try:
                    data = response.json()
                except ValueError as e:
                    logging.error(f"Invalid JSON format in {url}: {e}")
                    continue
                if isinstance(data, dict):
                    data = next((v for v in data.values() if isinstance(v, list)), [])
                for item in data if isinstance(data, list) else []:
                    if not isinstance(item, dict):
                        continue
                    server = item.get('host') or item.get('server') or item.get('ip')
                    port, secret = item.get('port'), item.get('secret')
                    if server and port and secret:
                        parsed = parse_proxy_link(f"tg://proxy?server={server}&port={port}&secret={secret}")
                        if parsed:
                            found.append(parsed)
            else:
                for line in response.text.splitlines():
                    for link in LINK_RE.findall(html.unescape(line)):
                        parsed = parse_proxy_link(link)
                        if parsed:
                            found.append(parsed)
            logging.info(f"Found {len(found)} proxy links in {url}")
        except requests.RequestException as e:
            logging.error(f"HTTP error fetching {url}: {e}")
        candidates.extend(found)
        time.sleep(random.uniform(0.5, 1.0))
    return candidates


def fetch_candidates_from_telegram_channel(url):
    """Read a public channel preview page (t.me/s/...). Returns unchecked tuples."""
    found = []
    try:
        logging.info(f"Opening {url} with HTTP Request")
        response = requests.get(url, headers={'User-Agent': get_random_user_agent()}, timeout=15)
        response.raise_for_status()
        if "recaptcha" in response.text.lower():
            logging.warning(f"CAPTCHA detected on {url}")

        soup = BeautifulSoup(response.text, 'html.parser')
        for element in soup.find_all('a', href=True):
            parsed = parse_proxy_link(element['href'])
            if parsed:
                found.append(parsed)
        logging.info(f"Found {len(found)} proxy links in {url}")
    except requests.RequestException as e:
        logging.error(f"HTTP error fetching {url}: {e}")
    except Exception as e:
        logging.error(f"General error fetching {url}: {e}")
    time.sleep(random.uniform(0.5, 1.0))
    return found


def filter_online(candidates):
    """Remove duplicates, test each proxy once (in parallel) and return the online links."""
    unique = {}
    for server, port, secret in candidates:
        key_secret = secret.lower() if HEX_RE.match(secret) else secret
        unique.setdefault((server.lower(), port, key_secret), (server, port, secret))
    logging.info(f"Testing {len(unique)} unique proxies (from {len(candidates)} links)")

    online = []
    with ThreadPoolExecutor(max_workers=CHECK_WORKERS) as executor:
        futures = {executor.submit(check_proxy_status, s, p): (s, p, sec) for s, p, sec in unique.values()}
        for future in as_completed(futures):
            try:
                if future.result():
                    online.append(make_link(*futures[future]))
            except Exception as e:
                logging.error(f"Error checking proxy {futures[future]}: {e}")
    logging.info(f"{len(online)} of {len(unique)} proxies are online")
    return online


def source_label(url):
    parts = urlparse(url)
    if parts.netloc == 'raw.githubusercontent.com':
        return '/'.join(parts.path.strip('/').split('/')[:2])
    return parts.netloc + parts.path


def save_proxies_to_file(proxy_list, filename=DEFAULT_PROXY_PATH):
    try:
        unique_proxies = sorted(set(proxy_list))
        with open(filename, 'w', encoding='utf-8') as file:
            for proxy in unique_proxies:
                file.write(proxy + '\n')
        logging.info(f"Saved {len(unique_proxies)} unique proxies to {filename}")
        return unique_proxies
    except IOError as e:
        logging.error(f"Error writing to {filename}: {e}")
        return []

def update_readme(proxy_list, filename=DEFAULT_README_PATH):
    try:
        utc_now = datetime.now(pytz.UTC)
        iran_tz = pytz.timezone('Asia/Tehran')
        iran_now = utc_now.astimezone(iran_tz)
        
        jalali_date = jdatetime.datetime.fromgregorian(datetime=iran_now)
        update_time_iran = jalali_date.strftime('%H:%M %d-%m-%Y')
        logging.info(f"Updating README with Iranian timestamp: {update_time_iran}")

        sample_proxies = random.sample(proxy_list, min(20, len(proxy_list))) if proxy_list else []
        table_rows = ""
        valid_proxies = 0
        for i, proxy in enumerate(sample_proxies, 1):
            parsed = parse_proxy_link(proxy)
            if parsed:
                server, port, secret = parsed
                display_proxy = make_link(server, port, secret)
                table_rows += f"| {i} | `{server}` | `{port}` | ✅ فعال | [لینک پروکسی]({display_proxy}) |\n"
                valid_proxies += 1
            else:
                logging.warning(f"Invalid proxy format, skipped: {proxy}")

        logging.info(f"Added {valid_proxies} valid proxies to the table (out of {len(sample_proxies)} sampled)")

        text_sources_md = "\n".join(f"  - [{source_label(u)}]({u})" for u in TEXT_URLS)
        channels_md = ", ".join(u.rstrip('/').split('/')[-1] for u in TELEGRAM_URLS)

        readme_content = f"""# 📊 نتایج استخراج: (آخرین بروزرسانی: {update_time_iran})



این پروژه یک اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع متنی و کانال‌های تلگرام است. پروکسی‌ها در فایل `proxy.txt` ذخیره می‌شوند و هر 3 ساعت به‌صورت خودکار به‌روزرسانی می‌شوند.

## ✨ درباره پروژه

این اسکریپت با استفاده از `requests` برای منابع متنی و کانال‌های تلگرام، پروکسی‌های MTProto را جمع‌آوری می‌کند. پروکسی‌های تکراری حذف شده و نتایج در فایل `proxy.txt` ذخیره می‌شوند. این فرآیند به‌صورت خودکار با **GitHub Actions** هر 3 ساعت اجرا می‌شود.

## 🚀 ویژگی‌ها
- 🌐 جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- 🔄 به‌روزرسانی خودکار هر 3 ساعت
- 🗑 حذف پروکسی‌های تکراری
- 🔑 بدون نیاز به API تلگرام
- 📱 مناسب برای کاربران در جستجوی پروکسی‌های فعال MTProto

## 📋 پیش‌نیازها
- 🐍 پایتون 3.11
- 📦 کتابخانه‌های مورد نیاز: `requests`, `beautifulsoup4`, `pytz`, `jdatetime`
- نصب وابستگی‌ها با: `pip install -r requirements.txt`

## 🛠 نحوه استفاده
1. فایل `proxy.txt` را از [اینجا](proxy.txt) دانلود کنید.
2. لینک‌های پروکسی (با فرمت `tg://proxy?...` یا `https://t.me/proxy?...`) را در کلاینت تلگرام وارد کنید.
3. در جدول زیر، روی لینک‌های ستون **لینک پروکسی** کلیک کنید تا به تلگرام هدایت شوید یا لینک را کپی کنید.
4. برای به‌روزرسانی دستی، به تب **Actions** در مخزن بروید و روی **Run workflow** کلیک کنید.

## 🌍 منابع پروکسی
- **منابع متنی**:
{text_sources_md}
- **کانال‌های تلگرام**:
  - {channels_md}

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
{table_rows}

> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
"""

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(readme_content)
        logging.info("Successfully updated README.md with new styling and Iranian date format")
    except Exception as e:
        logging.error(f"Error updating README.md: {e}")

if __name__ == "__main__":
    candidates = fetch_candidates_from_text_urls(TEXT_URLS)
    for channel_url in TELEGRAM_URLS:
        candidates.extend(fetch_candidates_from_telegram_channel(channel_url))
    logging.info(f"Collected {len(candidates)} proxy links in total")

    online_proxies = filter_online(candidates)

    if not online_proxies:
        # never overwrite the previous good list with an empty one (e.g. network outage)
        logging.error("No online proxies found - keeping the existing proxy.txt and README.md")
        sys.exit(1)

    all_proxies = save_proxies_to_file(online_proxies)
    update_readme(all_proxies)
