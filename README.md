# 📊 نتایج استخراج: (آخرین بروزرسانی: 21:01 05-09-1405)



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
| 1 | `rocket.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rocket.telehelp.top&port=443&secret=ee891ce9e0f5fc9fb12e2439fa002d173864726976652e676f6f676c652e636f6d) |
| 2 | `85.133.200.47` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.47&port=8880&secret=dd1603010200010001fc030386e24c3add) |
| 3 | `shish.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shish.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 4 | `ir-ir.grumpyoldmen.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.grumpyoldmen.info&port=8443&secret=104462821249bd7ac519130220c8dd09) |
| 5 | `api.mangoseason5.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.mangoseason5.co.uk&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 6 | `162.55.45.247` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=162.55.45.247&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `no-problem.ir.aojsnqzcdsc.info` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=no-problem.ir.aojsnqzcdsc.info&port=88&secret=ee0000f00f0f775555fffffff5006e2e69626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `tech.gooodrat.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tech.gooodrat.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `old.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=old.graduat.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 11 | `rudmoain.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rudmoain.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 12 | `philadelphia.hezarto.info` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=philadelphia.hezarto.info&port=5500&secret=ec742282124f04d318551341ead76457) |
| 13 | `maraka16.ashwren.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=maraka16.ashwren.xyz&port=443&secret=ee912defad667a620d66dbf5fd0b2a1bcc62726f777365722e79616e6465782e7275) |
| 14 | `83.243.86.212` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=83.243.86.212&port=7443&secret=79e344818749bd7ac519130220c25d09) |
| 15 | `o06d9opx.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=o06d9opx.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `731.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=731.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `85.133.194.5` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.194.5&port=2020&secret=00000000000000000000000000000000) |
| 18 | `for.you.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=for.you.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `pebble.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pebble.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c94706562626c652e76656c76657477696e646f772e6363) |
| 20 | `naznazi.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=naznazi.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
