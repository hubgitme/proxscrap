# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:59 06-09-1405)



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
| 1 | `char.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.anotelinopalk.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 2 | `its.fastprx.co.uk` | `2086` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=its.fastprx.co.uk&port=2086&secret=d2289d65c760a8245e24ffc2e3a3ba27) |
| 3 | `se.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.anotelinopalk.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 4 | `red.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=red.telehelp.top&port=443&secret=eefa58f5720fab51caf38ad09ee80c16d964726976652e676f6f676c652e636f6d) |
| 5 | `209.94.61.21` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=209.94.61.21&port=443&secret=ee3db86f433b3aeb5c115185432b0ca1db636c6f7564666c6172652e636f6d) |
| 6 | `box-to-box.dablecheckz.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=box-to-box.dablecheckz.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 7 | `o09opx.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=o09opx.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `api.mangoseason5.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.mangoseason5.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `dune.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dune.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9464756e652e76656c76657477696e646f772e6363) |
| 10 | `sudoaptupdate-y-sudoaptupgrade-y.logmanfi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sudoaptupdate-y-sudoaptupgrade-y.logmanfi.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 11 | `matrixxx.wtf` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=matrixxx.wtf&port=443&secret=ee9250b2b65b8921d01a306376fc2dd2ca6d617472697878782e777466) |
| 12 | `se.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `116.202.246.219` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.202.246.219&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `87.248.144.60` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.60&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 15 | `benze-benz.ir.osahflahyev.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=benze-benz.ir.osahflahyev.info&port=7443&secret=79e344818749bd7ac519130220c25d09) |
| 16 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 17 | `41.hide.7y76y.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=41.hide.7y76y.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `87.248.144.158` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.158&port=8880&secret=3XnjRIGHSb16xRkTAiDCXQk) |
| 19 | `65.21.227.250` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.21.227.250&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 20 | `sushima.ferdosisets.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sushima.ferdosisets.info&port=8443&secret=1603010200010001fc030386e24c3add) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
