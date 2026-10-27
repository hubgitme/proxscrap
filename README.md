# 📊 نتایج استخراج: (آخرین بروزرسانی: 03:44 05-08-1405)



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
| 1 | `philadelphia.hezarto.info` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=philadelphia.hezarto.info&port=5500&secret=7HQighJPBNMYVRNB6tdkVw) |
| 2 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 3 | `noon.begir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noon.begir.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 4 | `gov.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gov.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 5 | `rootssh2.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rootssh2.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `good.cipservice.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=good.cipservice.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `dizgrakh.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dizgrakh.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `sn.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sn.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `s3.saalaad.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.saalaad.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `hash.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hash.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `iro.varfootball2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iro.varfootball2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `app.telbet.app` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.telbet.app&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `ir.forzajuve.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.forzajuve.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 14 | `s3.soft98.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.soft98.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `ir-ir.panhandleflyers.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.panhandleflyers.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 16 | `royaclinic.beauty` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=royaclinic.beauty&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `Anahita.ir.awedsj.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Anahita.ir.awedsj.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `toleka79.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=toleka79.mosswren.vip&port=443&secret=ee6ce7aa9636179a5f67366aaab4702a26746f6c656b6137392e6d6f73737772656e2e766970) |
| 19 | `sukari30.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sukari30.tidelark.cc&port=443&secret=ee14697011e0c73f03e95d7b6919a2252b73756b61726933302e746964656c61726b2e6363) |
| 20 | `baran.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=baran.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
