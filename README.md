# 📊 نتایج استخراج: (آخرین بروزرسانی: 12:46 09-08-1405)



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
| 1 | `you.nasakhamia.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=you.nasakhamia.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `name.namenewok.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.namenewok.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `Cu.mp.6h.sp.4d.mip.ts5.f2h.gk.w.13-905-33-84.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Cu.mp.6h.sp.4d.mip.ts5.f2h.gk.w.13-905-33-84.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `hash.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hash.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `team.fast--pro.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=team.fast--pro.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 6 | `new.nakoskoskesh.co.uk` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.nakoskoskesh.co.uk&port=8080&secret=EERighJJvXrFGRMCIMJdCQ) |
| 7 | `leomessi.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=leomessi.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `star.telbet.lol` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=star.telbet.lol&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `Rostam.ir.igakwvwa.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Rostam.ir.igakwvwa.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `21.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=21.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `makama85.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=makama85.mosswren.vip&port=443&secret=eeb8e5365580b9ad3c2ee355dfcbc245e56d616b616d6138352e6d6f73737772656e2e766970) |
| 12 | `ir-ir.radio-zvez.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.radio-zvez.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 13 | `dashi.estabonita.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dashi.estabonita.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 14 | `premium.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `dpi.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dpi.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 16 | `PAyDaR.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=PAyDaR.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `craft.malavanann.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=craft.malavanann.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `old.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=old.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `amoo.bingi.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=amoo.bingi.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 20 | `max.kimt.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=max.kimt.click&port=443&secret=ee1b153cf06dbd43c6085c359a6702eb936d61782e6b696d742e636c69636b) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
