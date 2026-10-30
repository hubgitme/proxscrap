# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:37 08-08-1405)



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
| 1 | `zotoma94.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zotoma94.mosswren.vip&port=443&secret=ee14697011e0c73f03e95d7b6919a2252b7a6f746f6d6139342e6d6f73737772656e2e766970) |
| 2 | `ramane52.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ramane52.mosswren.vip&port=443&secret=eeae5ab45be1bccbba85eec21085b2fd2072616d616e6535322e6d6f73737772656e2e766970) |
| 3 | `leloto39.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=leloto39.mosswren.vip&port=443&secret=ee920a4026fcc79354d87c30db9280e5786c656c6f746f33392e6d6f73737772656e2e766970) |
| 4 | `stone.quietfjord.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=stone.quietfjord.click&port=443&secret=ee1c0302da542b3dbfa43927dfa654feaf73746f6e652e7175696574666a6f72642e636c69636b) |
| 5 | `FOR-IRAN.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=FOR-IRAN.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `178.105.127.56` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.127.56&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 7 | `731.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=731.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `bimeh.my-moon.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bimeh.my-moon.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `dokhtar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dokhtar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 10 | `MAP.cooptoop.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=MAP.cooptoop.site&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 11 | `pofak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pofak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 12 | `bookmook.hichibehichi-co.info` | `2882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bookmook.hichibehichi-co.info&port=2882&secret=dd10400103324995b07c030386e886e7f1) |
| 13 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `cdn1.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn1.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `paeez.delroba.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=paeez.delroba.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `behtarin.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=behtarin.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `royaclinic.beauty` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=royaclinic.beauty&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `sn.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sn.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
