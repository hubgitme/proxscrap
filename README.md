# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:43 02-08-1405)



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
| 1 | `ponyny28.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ponyny28.tidelark.cc&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd1706f6e796e7932382e746964656c61726b2e6363) |
| 2 | `65.109.147.34` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.147.34&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 3 | `ghoghnoos.ir.awedsj.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ghoghnoos.ir.awedsj.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `vilomi57.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vilomi57.tidelark.cc&port=443&secret=ee6ce7aa9636179a5f67366aaab4702a2676696c6f6d6935372e746964656c61726b2e6363) |
| 5 | `tokane46.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tokane46.tidelark.cc&port=443&secret=eeae5ab45be1bccbba85eec21085b2fd20746f6b616e6534362e746964656c61726b2e6363) |
| 6 | `ir.xn--ds-bja.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.xn--ds-bja.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 7 | `redflag.yazaebalsyadelatproxy.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.co.uk&port=443&secret=ee69e899d89ec68e220ca177557322b27f726564666c61672e79617a616562616c73796164656c617470726f78792e6363) |
| 8 | `fruit.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fruit.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `jadide.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadide.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `195.18.10.204` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.18.10.204&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |
| 11 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 12 | `ir-ir.pbdjarum.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.pbdjarum.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 13 | `91.107.171.35` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.171.35&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 14 | `ccc7h6.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ccc7h6.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 15 | `ssh.meow0.co.uk` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ssh.meow0.co.uk&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 16 | `shampoo.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shampoo.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `ir.ariely.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.ariely.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 18 | `shoes.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shoes.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `ponyzo32.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ponyzo32.tidelark.cc&port=443&secret=eeb8e5365580b9ad3c2ee355dfcbc245e5706f6e797a6f33322e746964656c61726b2e6363) |
| 20 | `95.217.193.223` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.193.223&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
