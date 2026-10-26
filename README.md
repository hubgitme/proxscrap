# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:39 04-08-1405)



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
| 1 | `r3.soft98.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r3.soft98.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `hash.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hash.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `uh1l776.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=uh1l776.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `qazmel.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=qazmel.ir&port=443&secret=ee79e344818749bd7ac519130220c25d09706574726f732d65732e636f2e756b) |
| 5 | `luxuryman.sbs` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=luxuryman.sbs&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `cocorichmond.pareporeh.info` | `7799` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cocorichmond.pareporeh.info&port=7799&secret=dd10400103324995b07c030386e886e7f1) |
| 7 | `premium.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `sukari30.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sukari30.tidelark.cc&port=443&secret=ee14697011e0c73f03e95d7b6919a2252b73756b61726933302e746964656c61726b2e6363) |
| 9 | `sarzamin.mosbatbashim.info` | `2882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sarzamin.mosbatbashim.info&port=2882&secret=dd10400103324995b07c030386e886e7f1) |
| 10 | `pofak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pofak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 11 | `ponyzo32.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ponyzo32.tidelark.cc&port=443&secret=eeb8e5365580b9ad3c2ee355dfcbc245e5706f6e797a6f33322e746964656c61726b2e6363) |
| 12 | `kasu85.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kasu85.tidelark.cc&port=443&secret=eeb8e5365580b9ad3c2ee355dfcbc245e56b61737538352e746964656c61726b2e6363) |
| 13 | `ir-ir.macauley.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.macauley.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 14 | `on.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=on.mishutkin.click&port=443&secret=eebc740653e2e1fd5972b4a92e5a0dd7826f6e2e6d69736875746b696e2e636c69636b) |
| 15 | `server2.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server2.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 16 | `yek.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yek.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `reyhoon.shambelile.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=reyhoon.shambelile.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 18 | `hadaf.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hadaf.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `rf.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rf.mishutkin.click&port=443&secret=ee5a994c9e79b5e3ff7ec78e7d7e77eb0b72662e6d69736875746b696e2e636c69636b) |
| 20 | `noon.begir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noon.begir.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
