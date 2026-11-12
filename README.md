# 📊 نتایج استخراج: (آخرین بروزرسانی: 09:12 21-08-1405)



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
| 1 | `origin.mossharbor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=origin.mossharbor.xyz&port=8443&secret=ee1c0302da542b3dbfa43927dfa654feaf786170692e6f7a6f6e2e7275) |
| 2 | `xe1rn.proxydazhenaparkovke.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=xe1rn.proxydazhenaparkovke.site&port=443&secret=ee4a26ea6bb803e4d556b56178d75a0889786531726e2e70726f787964617a68656e617061726b6f766b652e73697465) |
| 3 | `130.210.28.61` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=130.210.28.61&port=8443&secret=ee93347c71bba50740c51ae7052ed6b9e3636c6f7564666c6172652e636f6d) |
| 4 | `ir.lv223.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.lv223.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 5 | `leomessi.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=leomessi.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `gishniz.shambelile.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gishniz.shambelile.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 7 | `star.talebi.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=star.talebi.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `78.47.131.70` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=78.47.131.70&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `vasle.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vasle.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `becarefull.bypased.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=becarefull.bypased.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 11 | `91.98.101.34` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.101.34&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `turbo.webproxy.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=turbo.webproxy.lol&port=443&secret=ee51fa3aadf3d9849a914784a8de1ff7e0747572626f2e77656270726f78792e6c6f6c) |
| 13 | `rimi88.fernlark.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rimi88.fernlark.xyz&port=8443&secret=ee3e175e0503b04fc22a65e6b6b60d5d9c786170692e6f7a6f6e2e7275) |
| 14 | `boost.webproxy.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boost.webproxy.lol&port=443&secret=ee61a214279f303f07c536ce7a8228e4c5626f6f73742e77656270726f78792e6c6f6c) |
| 15 | `soh5.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soh5.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `88.99.126.37` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.126.37&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `worldmaster.varomax.co.uk` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=worldmaster.varomax.co.uk&port=5500&secret=eeRigzNJvXrFGRMCIMJdEA) |
| 18 | `irogallery.golgoli1.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irogallery.golgoli1.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `vizhzhzhzhzh.bypased.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vizhzhzhzhzh.bypased.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 20 | `MAP.cooptoop.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=MAP.cooptoop.site&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
