# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:36 06-08-1405)



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
| 1 | `speed.runserver.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=speed.runserver.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `aseman.lunavane.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aseman.lunavane.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `nocloudnew.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nocloudnew.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `craft.malavanann.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=craft.malavanann.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `s3.saalaad.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.saalaad.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `new7.mizanmizanesgh.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new7.mizanmizanesgh.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `male58.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=male58.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e6d616c6535382e6d6f73737772656e2e766970) |
| 8 | `41.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=41.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `char.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `ir.lv223.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.lv223.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 11 | `3etare.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3etare.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `ir.forzajuve.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.forzajuve.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 13 | `delvari.ir.aysghfkzcxg.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=delvari.ir.aysghfkzcxg.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `web-kook.mosbatbashim.info` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web-kook.mosbatbashim.info&port=5500&secret=DDBighLLvXrFGRMCBVJdFQ) |
| 15 | `kaveh-ahangar.ir.aysghfkzcxg.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kaveh-ahangar.ir.aysghfkzcxg.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `pashmak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pashmak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `Dho.phd.iv.md.h.g.if.7.www1www.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Dho.phd.iv.md.h.g.if.7.www1www.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `ir-ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdC) |
| 19 | `amoo.bingi.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=amoo.bingi.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 20 | `web.mangoseason7.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.mangoseason7.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
