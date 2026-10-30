# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:20 08-08-1405)



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
| 1 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `d1.jadroom.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=d1.jadroom.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 3 | `ir.speed.finecooking.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.speed.finecooking.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 4 | `noon.begir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noon.begir.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 5 | `196.19.243.197` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=196.19.243.197&port=443&secret=7j2yWGeEZqfM65fTER6Yy5t3aWxkYmVycmllcy5ydQ) |
| 6 | `dizgrakh.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dizgrakh.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `bastani.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bastani.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 8 | `ir.closcloud.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.closcloud.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 10 | `sulone58.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sulone58.tidelark.cc&port=443&secret=ee24c8636b7e946779a023ee708370719b73756c6f6e6535382e746964656c61726b2e6363) |
| 11 | `49.12.36.40` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.12.36.40&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 12 | `haf.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haf.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `ir-ir.grumpyoldmen.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.grumpyoldmen.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 14 | `zero.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zero.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `ahvaz.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ahvaz.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `ir.xn--ds-bja.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.xn--ds-bja.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 17 | `maxspeed.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=maxspeed.proxynet.tech&port=443&secret=ee7fff194939ff56c5f70281d7b20f575c6d617873706565642e70726f78796e65742e74656368) |
| 18 | `Strait-of-Hormuz.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Strait-of-Hormuz.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `ving.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ving.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `api.mangoseason5.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.mangoseason5.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
