# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:11 23-08-1405)



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
| 1 | `AZADI.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AZADI.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `vimika15.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vimika15.tidelark.cc&port=443&secret=ee4abe44348ba405ac59448f7f9fe6353c706574726f766963682e7275) |
| 3 | `195.18.10.204` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.18.10.204&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |
| 4 | `philadelphia.hezarto.info` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=philadelphia.hezarto.info&port=5500&secret=7HQighJPBNMYVRNB6tdkVw) |
| 5 | `api.mangoseason5.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.mangoseason5.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `refiq.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=refiq.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 7 | `ghasam-be-shab.hosiyaman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ghasam-be-shab.hosiyaman.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 8 | `ir.mohearn.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.mohearn.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 9 | `avangard.pareporeh.info` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=avangard.pareporeh.info&port=5500&secret=7HQighJPBNMYVRNB6tdkVw) |
| 10 | `vivo.xeonxu.site` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vivo.xeonxu.site&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 11 | `206.71.149.70` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=206.71.149.70&port=8080&secret=vshsJGsgKdnhsKenbsYrbbxhdYsbdb2LanndgsfdhAAAAeee) |
| 12 | `shoes.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shoes.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `731.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=731.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `origin.mossharbor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=origin.mossharbor.xyz&port=8443&secret=ee1c0302da542b3dbfa43927dfa654feaf786170692e6f7a6f6e2e7275) |
| 15 | `edgespindle.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=edgespindle.org&port=443&secret=eebec6acb2a5464709485d7cbeedd8612b686f66662e7275) |
| 16 | `ir.peachsoft.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.peachsoft.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 17 | `baran.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=baran.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `raleto69.fernlark.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=raleto69.fernlark.xyz&port=443&secret=ee8ac4f89d6036e07f6ff9e00b1699819e706574726f766963682e7275) |
| 19 | `65.109.98.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.98.231&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 20 | `ir.barhousefarm.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.barhousefarm.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
