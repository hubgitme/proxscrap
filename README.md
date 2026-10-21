# 📊 نتایج استخراج: (آخرین بروزرسانی: 20:06 29-07-1405)



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
| 1 | `ahvaz.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ahvaz.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `hash.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hash.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `cr777.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cr777.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `noh.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noh.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `aseman.lunavane.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aseman.lunavane.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `ssh.meow0.co.uk` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ssh.meow0.co.uk&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 7 | `ir.gnutella2.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.gnutella2.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 8 | `soh5.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soh5.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `e.networkmodeai.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=e.networkmodeai.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `ponyny28.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ponyny28.tidelark.cc&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd1706f6e796e7932382e746964656c61726b2e6363) |
| 11 | `iranmaster27.suser.ir` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iranmaster27.suser.ir&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 12 | `redflag.yazaebalsyadelatproxy.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e726564666c61672e79617a616562616c73796164656c617470726f78792e766970) |
| 13 | `www.www1www.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.www1www.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 14 | `ir.xn--ds-bja.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.xn--ds-bja.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 15 | `13.141.35.204` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=13.141.35.204&port=443&secret=ee3f8a91c2d7e04b6a9f12c5e8370bd4aa786170692e6f7a6f6e2e7275) |
| 16 | `ll6j.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ll6j.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `103.161.35.23` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=103.161.35.23&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 18 | `kabab.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kabab.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 19 | `lode46.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lode46.mosswren.vip&port=443&secret=ee6ce7aa9636179a5f67366aaab4702a266c6f646534362e6d6f73737772656e2e766970) |
| 20 | `do.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=do.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
