# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:16 02-09-1405)



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
| 1 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `edgespindle.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=edgespindle.org&port=443&secret=eebec6acb2a5464709485d7cbeedd8612b686f66662e7275) |
| 3 | `age.nine11.art` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=age.nine11.art&port=443&secret=5b0a98d9fa4771fad9402dc3dedbdd9a) |
| 4 | `hapoo.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hapoo.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 5 | `95.217.193.214` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.193.214&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 6 | `a2.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a2.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `41.hide.7y76y.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=41.hide.7y76y.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `21.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=21.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `baran.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=baran.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `zenon.flashspder.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zenon.flashspder.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 11 | `s2.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s2.server-space52.info&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 12 | `6h.pe.3.fi.u.fp.66-84-5-947.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6h.pe.3.fi.u.fp.66-84-5-947.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `0000way.iraj.trsr57d.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=0000way.iraj.trsr57d.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `matrixxx.wtf` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=matrixxx.wtf&port=443&secret=ee9250b2b65b8921d01a306376fc2dd2ca6d617472697878782e777466) |
| 15 | `www.torbad.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.torbad.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 16 | `lol-lock.godserver52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lol-lock.godserver52.info&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 17 | `46.225.35.245` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.35.245&port=443&secret=YyEEgYdJXfrFmgMCIMJdjjRueWVrdGFuZXQA) |
| 18 | `sn.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sn.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `refiq.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=refiq.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 20 | `45.83.85.233` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.83.85.233&port=443&secret=31abec0f24f6e02870e523711c3be0d4) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
