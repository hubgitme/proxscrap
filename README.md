# 📊 نتایج استخراج: (آخرین بروزرسانی: 19:02 03-08-1405)



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
| 1 | `star.talebi.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=star.talebi.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `noh.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noh.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `hash.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hash.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `uwu.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=uwu.mishutkin.click&port=443&secret=eec21a6ac829a6acfe1077910fc3da1c127577752e6d69736875746b696e2e636c69636b) |
| 5 | `aseman.lunavane.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aseman.lunavane.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `ir.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `org.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=org.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `e3fand.fesgheli.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=e3fand.fesgheli.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `wifi.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=wifi.mishutkin.click&port=443&secret=eeaafcdfaabd4ba41103eeb581537dc940776966692e6d69736875746b696e2e636c69636b) |
| 10 | `r3.soft98.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r3.soft98.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `great.cipservice.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=great.cipservice.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `from.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=from.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `167.235.255.168` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.235.255.168&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `reyhoon.shambelile.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=reyhoon.shambelile.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 15 | `r3.saalaad.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r3.saalaad.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `good.cipservice.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=good.cipservice.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `tassian.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tassian.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `premium.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `connect.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.mishutkin.click&port=443&secret=ee43b48df152c2246a45ec2f88ea52877264726976652e676f6f676c652e636f6d) |
| 20 | `fast.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.mishutkin.click&port=443&secret=eef767ebee5708dadc985d58ad6e04560664726976652e676f6f676c652e636f6d) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
