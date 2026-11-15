# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:14 24-08-1405)



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
| 1 | `89.167.69.210` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.167.69.210&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `84.201.14.50` | `8446` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=84.201.14.50&port=8446&secret=ee1a41219b6c5d619c8e11a8e40356e45d7777772e6d6963726f736f66742e636f6d) |
| 3 | `194.120.230.120` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.120&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 4 | `rad.irani-pr.net` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rad.irani-pr.net&port=85&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `dokhtar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dokhtar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 6 | `cloud93.aaifx.com` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cloud93.aaifx.com&port=8443&secret=ee6a175bc5a503dd59e6620ac3d3f42b73636c6f7564666c6172652e636f6d) |
| 7 | `ir.forzajuve.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.forzajuve.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 8 | `613.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=613.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `worldmaster.varomax.co.uk` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=worldmaster.varomax.co.uk&port=5500&secret=eeRigzNJvXrFGRMCIMJdEA) |
| 10 | `yek.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yek.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `ABOUT.Roo3beh.blog` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ABOUT.Roo3beh.blog&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `143.14.59.80` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=143.14.59.80&port=8080&secret=vshsJGsgKdnhsKenbsYrbbxhdYsbdb2LanndgsfdhAAAAeee) |
| 13 | `hapoo.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hapoo.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 14 | `name.namenewok.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.namenewok.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `proxy.foriran.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.foriran.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 16 | `suka90.mossharbor.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=suka90.mossharbor.xyz&port=443&secret=ee33e69fd218748e738b564b82cabecf47786170692e6f7a6f6e2e7275) |
| 17 | `jadid.zhigool.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadid.zhigool.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 18 | `jhndoes.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jhndoes.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `neka92.larchmere.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=neka92.larchmere.xyz&port=8443&secret=eeb26dd44a039e6125d490c0aeaa262559786170692e6f7a6f6e2e7275) |
| 20 | `65.21.227.250` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.21.227.250&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
