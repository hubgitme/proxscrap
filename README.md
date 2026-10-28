# 📊 نتایج استخراج: (آخرین بروزرسانی: 07:26 06-08-1405)



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
| 1 | `tazenafas.dingi3.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tazenafas.dingi3.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `ir-ir.rebol.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.rebol.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `46.225.148.183` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.148.183&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `from.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=from.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `ir.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 6 | `baran.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=baran.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 8 | `AVA.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AVA.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `ir-ir.grumpyoldmen.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.grumpyoldmen.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 10 | `web-kook.mosbatbashim.info` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web-kook.mosbatbashim.info&port=5500&secret=DDBighLLvXrFGRMCBVJdFQ) |
| 11 | `pnj.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `ll6j.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ll6j.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `server2.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server2.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 14 | `ahvaz.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ahvaz.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `north.velvetoak.work` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=north.velvetoak.work&port=443&secret=eee37d2ac00492bf7c77672c84a4a00c436e6f7274682e76656c7665746f616b2e776f726b) |
| 16 | `toleka79.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=toleka79.mosswren.vip&port=443&secret=ee6ce7aa9636179a5f67366aaab4702a26746f6c656b6137392e6d6f73737772656e2e766970) |
| 17 | `sefid.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sefid.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `good.cipservice.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=good.cipservice.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `honar.saheledarya.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=honar.saheledarya.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `178.105.127.56` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.127.56&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
