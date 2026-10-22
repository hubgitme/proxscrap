# 📊 نتایج استخراج: (آخرین بروزرسانی: 20:07 30-07-1405)



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
| 1 | `vasle.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vasle.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `21.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=21.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `silnet.varfootball.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silnet.varfootball.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `nasho.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nasho.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 5 | `ir-ir.rebol.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.rebol.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 6 | `jadide.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadide.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `mahi.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mahi.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 8 | `craft.malavanann.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=craft.malavanann.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `gov.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gov.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 10 | `65.21.222.229` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.21.222.229&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 11 | `iro.varfootball2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iro.varfootball2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `135.181.154.26` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.154.26&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `95.217.193.223` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.193.223&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 14 | `ir.gnutella2.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.gnutella2.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 15 | `my-iran.vingardium.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=my-iran.vingardium.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 16 | `e.networkmodeai.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=e.networkmodeai.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `rade94.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rade94.tidelark.cc&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b7261646539342e746964656c61726b2e6363) |
| 18 | `ahvaz.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ahvaz.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `daliran-tangestan.ir.aysghfkzcxg.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=daliran-tangestan.ir.aysghfkzcxg.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `rf.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rf.mishutkin.click&port=443&secret=ee5a994c9e79b5e3ff7ec78e7d7e77eb0b72662e6d69736875746b696e2e636c69636b) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
