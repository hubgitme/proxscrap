# 📊 نتایج استخراج: (آخرین بروزرسانی: 17:02 20-08-1405)



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
| 1 | `lomavi84.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lomavi84.mosswren.vip&port=443&secret=ee24c8636b7e946779a023ee708370719b6c6f6d61766938342e6d6f73737772656e2e766970) |
| 2 | `aseman.lunavane.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aseman.lunavane.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `rad.irani-pr.net` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rad.irani-pr.net&port=85&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `ir.lv223.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.lv223.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 5 | `telegram.telbet.app` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=telegram.telbet.app&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `mikaga72.larchmere.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mikaga72.larchmere.xyz&port=443&secret=eee2bb975ea85e1dc2466cf7f309ce6b95706574726f766963682e7275) |
| 7 | `losuny65.quietfjord.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=losuny65.quietfjord.click&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b786170692e6f7a6f6e2e7275) |
| 8 | `hapoo.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hapoo.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 9 | `premium.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `Gos.8f.dk.euv.4h.d.kw.68-309-27-46.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Gos.8f.dk.euv.4h.d.kw.68-309-27-46.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `88.99.125.62` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.125.62&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `0000way.iraj.trsr57d.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=0000way.iraj.trsr57d.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `nemazo76.larchmere.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nemazo76.larchmere.xyz&port=443&secret=ee44f33295547b09ac13649a4c51c296f6706574726f766963682e7275) |
| 14 | `new7.mizanmizanesgh.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new7.mizanmizanesgh.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `app.webproxy.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.webproxy.lol&port=443&secret=ee176aff89de055a87d06876140d3a93f864726976652e676f6f676c652e636f6d) |
| 16 | `refiq.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=refiq.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `5go.hs.ydw.pf4.sgj.fi.t.reallygood.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5go.hs.ydw.pf4.sgj.fi.t.reallygood.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 19 | `diffluence.dniester.liz.outwash.paternal.pinoyteleseryelove.com` | `3200` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=diffluence.dniester.liz.outwash.paternal.pinoyteleseryelove.com&port=3200&secret=dd73825b27d1e500fe52ba4cb1b0138568) |
| 20 | `ahvaz.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ahvaz.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
