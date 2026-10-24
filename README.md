# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:41 02-08-1405)



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
| 1 | `puot.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=puot.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `333.antony-gordon.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=333.antony-gordon.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `maka61.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=maka61.tidelark.cc&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e6d616b6136312e746964656c61726b2e6363) |
| 4 | `star.talebi.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=star.talebi.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `paeez.delroba.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=paeez.delroba.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `irogallery.golgoli1.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irogallery.golgoli1.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `159.69.9.248` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=159.69.9.248&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `dashi.estabonita.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dashi.estabonita.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 9 | `ir-ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdC) |
| 10 | `65.109.147.34` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.147.34&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 11 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 12 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `park.monik.hamintori.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=park.monik.hamintori.co.uk&port=443&secret=7l984oosSBbGySPf1NVjDgE=) |
| 14 | `PAyDaR.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=PAyDaR.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `topo15.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=topo15.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e746f706f31352e6d6f73737772656e2e766970) |
| 16 | `f123.e7.yayayajd.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=f123.e7.yayayajd.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `ir-ir.xn--ds-bja.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.xn--ds-bja.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 18 | `ir.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `hadaf.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hadaf.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `41.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=41.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
