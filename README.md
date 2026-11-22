# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:52 02-09-1405)



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
  - webproxy, iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn, asr_proxy, proxyskyy, MFDL000

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
| 1 | `vivi73.sorrelbay.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vivi73.sorrelbay.xyz&port=443&secret=ee2d41dffff1a709fab3857583bca0c360617669746f2e7275) |
| 2 | `lelo74.kelpmoor.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lelo74.kelpmoor.xyz&port=443&secret=eee38448c7e07ec8d42dfb2ca4d668b79062726f777365722e79616e6465782e7275) |
| 3 | `age.nine11.art` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=age.nine11.art&port=443&secret=86dbc3a5c345151b18f2843d8291c683) |
| 4 | `ir.barhousefarm.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.barhousefarm.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 5 | `mt-sw.alex-photo-notes.pl` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt-sw.alex-photo-notes.pl&port=443&secret=eeee677bf5d2356b3744e1208cc35d70887777772e676f6f676c652e636f6d) |
| 6 | `man-mamnon-misham-aziz.logmanfi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=man-mamnon-misham-aziz.logmanfi.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 7 | `MAP.cooptoop.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=MAP.cooptoop.site&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 8 | `91.221.191.138` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.221.191.138&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `www.reallygood.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.reallygood.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 10 | `731.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=731.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `ir.panhandleflyers.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.panhandleflyers.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 12 | `tassian.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tassian.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `vizhzhzhzhzh.bypased.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vizhzhzhzhzh.bypased.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 14 | `zenon.flashspder.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zenon.flashspder.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 15 | `ir-ir.flipme.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.flipme.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 16 | `Gos.8f.dk.euv.4h.d.kw.68-309-27-46.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Gos.8f.dk.euv.4h.d.kw.68-309-27-46.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `95.217.193.223` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.193.223&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 18 | `185.19.33.86` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.19.33.86&port=443&secret=eef08dee29bc748ad2f349c593e042bad87777772e6d6963726f736f66742e636f6d) |
| 19 | `hadaf.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hadaf.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `65.109.98.213` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.98.213&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
