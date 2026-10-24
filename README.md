# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:46 02-08-1405)



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
| 1 | `toleka79.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=toleka79.mosswren.vip&port=443&secret=ee6ce7aa9636179a5f67366aaab4702a26746f6c656b6137392e6d6f73737772656e2e766970) |
| 2 | `server2.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server2.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 3 | `sune79.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sune79.mosswren.vip&port=443&secret=eeb0a621aecd97816306c197d21a8bf47b73756e6537392e6d6f73737772656e2e766970) |
| 4 | `darya.saheledarya.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=darya.saheledarya.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `kasco.alhosein.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kasco.alhosein.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `wifi.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=wifi.mishutkin.click&port=443&secret=eeaafcdfaabd4ba41103eeb581537dc940776966692e6d69736875746b696e2e636c69636b) |
| 7 | `gavi88.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gavi88.mosswren.vip&port=443&secret=eeb8e5365580b9ad3c2ee355dfcbc245e56761766938382e6d6f73737772656e2e766970) |
| 8 | `ir.lv223.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.lv223.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 9 | `redflag.yazaebalsyadelatproxy.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.co.uk&port=443&secret=ee69e899d89ec68e220ca177557322b27f726564666c61672e79617a616562616c73796164656c617470726f78792e6363) |
| 10 | `mazo84.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mazo84.tidelark.cc&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b6d617a6f38342e746964656c61726b2e6363) |
| 11 | `65.109.147.39` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.147.39&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 12 | `exiscos.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=exiscos.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `167.235.197.46` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.235.197.46&port=8443&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `do.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=do.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `milo44.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=milo44.mosswren.vip&port=443&secret=eefd9a9e2ac2851ddc327fe5971e25a87d6d696c6f34342e6d6f73737772656e2e766970) |
| 16 | `core.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=core.proxynet.tech&port=443&secret=ee6963f54d30b8aa1edf4777718f519652636f72652e70726f78796e65742e74656368) |
| 17 | `digi.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `run.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=run.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `nyto59.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nyto59.mosswren.vip&port=443&secret=eefd9a9e2ac2851ddc327fe5971e25a87d6e79746f35392e6d6f73737772656e2e766970) |
| 20 | `loud-teal.godserver52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loud-teal.godserver52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
