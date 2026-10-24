# 📊 نتایج استخراج: (آخرین بروزرسانی: 02:23 03-08-1405)



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
| 1 | `bastani.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bastani.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 2 | `ir-ir.pbdjarum.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.pbdjarum.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `sumi71.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sumi71.mosswren.vip&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b73756d6937312e6d6f73737772656e2e766970) |
| 4 | `run.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=run.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `mashti.just-money.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mashti.just-money.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 6 | `ir-ir.naganuma.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.naganuma.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 7 | `r3.saalaad.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r3.saalaad.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `dokhtar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dokhtar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 9 | `s47n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s47n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `ir.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 11 | `ir-ir.my-pv.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.my-pv.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 12 | `char.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `craft.malavanann.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=craft.malavanann.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `Rostam.ir.igakwvwa.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Rostam.ir.igakwvwa.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `pnj.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `org.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=org.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `zovira85.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zovira85.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e7a6f7669726138352e6d6f73737772656e2e766970) |
| 18 | `tig.ofok.tui.frt.7fg7.88n.jananeman.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tig.ofok.tui.frt.7fg7.88n.jananeman.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `lenelo33.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lenelo33.mosswren.vip&port=443&secret=ee6ce7aa9636179a5f67366aaab4702a266c656e656c6f33332e6d6f73737772656e2e766970) |
| 20 | `159.69.9.248` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=159.69.9.248&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
