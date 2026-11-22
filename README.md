# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:46 02-09-1405)



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
| 1 | `194.120.230.37` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.37&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 2 | `ir.mohearn.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.mohearn.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `ram7.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ram7.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `my.soft98.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=my.soft98.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `joje.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=joje.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `dh1.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dh1.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `shsh.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shsh.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `isaco.ir.setado.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=isaco.ir.setado.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `ir-neverland.nowhearthis.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-neverland.nowhearthis.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 10 | `orchid.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=orchid.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946f72636869642e7061706572746561706f742e636f6d) |
| 11 | `www.gasolino.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.gasolino.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 12 | `16.new1.ramkal12.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=16.new1.ramkal12.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `silnet.varfootball.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silnet.varfootball.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `95.217.193.214` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.193.214&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 15 | `s3.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.server-space52.info&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 16 | `www.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.prxtg.top&port=443&secret=ee4274afdce63c4c3a2b341bad09220a047777772e70727874672e746f70) |
| 17 | `www.manazinjamiram.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.manazinjamiram.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 18 | `ir.panhandleflyers.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.panhandleflyers.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 19 | `47.83.158.121` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=47.83.158.121&port=443&secret=ee32f0f6ab5ca99f05bbee78eb54e2d5a0617a7572652e6d6963726f736f66742e636f6d) |
| 20 | `ir.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
