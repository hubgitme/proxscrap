# 📊 نتایج استخراج: (آخرین بروزرسانی: 20:54 16-08-1405)



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
  - [MhdiTaheri/ProxyCollector](https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt)
  - [SoliSpirit/mtproto](https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt)
  - [itsyebekhe.github.io/MTProtoNexus/extracted_proxies.json](https://itsyebekhe.github.io/MTProtoNexus/extracted_proxies.json)
  - [darkvibez456/mtproto-proxy-auto](https://raw.githubusercontent.com/darkvibez456/mtproto-proxy-auto/refs/heads/main/proxies.txt)
- **کانال‌های تلگرام**:
  - webproxy, iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn, asr_proxy, proxyskyy

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
| 1 | `135.181.74.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.74.189&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 2 | `pr.tr3v0.biz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pr.tr3v0.biz&port=443&secret=ee4e2568aa496237a954dcd0d5e7ad5f2670722e74723376302e62697a) |
| 3 | `lte.proxylite.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lte.proxylite.tech&port=443&secret=eed86f221b72fd35c363483cda02e5cee364726976652e676f6f676c652e636f6d) |
| 4 | `silver.ciaude.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silver.ciaude.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `31.57.166.178` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.57.166.178&port=443&secret=eedddddddddddddddddddddddddddddddd6d2e6265626f6f2e7275) |
| 6 | `dns.semqka.xyz` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dns.semqka.xyz&port=2083&secret=b8f7366edf8b63ba3a08d800b4ce355e) |
| 7 | `dokhtar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dokhtar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 8 | `portal.flashspder.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=portal.flashspder.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 9 | `nor-bala.flashspder.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nor-bala.flashspder.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 10 | `server2.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server2.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 11 | `00066f7k7.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=00066f7k7.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 12 | `Ulp.tz.9a.xu.cs.ir.jp.ir.ze8.ir.v6.8kmc.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ulp.tz.9a.xu.cs.ir.jp.ir.ze8.ir.v6.8kmc.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQAAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 13 | `nocloudnew.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nocloudnew.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `se.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `one.rozinalpoku.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=one.rozinalpoku.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6F6E652E726F7A696E616C706F6B752E636F2E756B) |
| 16 | `persian.gulf.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=persian.gulf.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `www.gasolino.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.gasolino.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 18 | `dizgrakh.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dizgrakh.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `leomessi.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=leomessi.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `621.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=621.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
