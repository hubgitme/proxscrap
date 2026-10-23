# 📊 نتایج استخراج: (آخرین بروزرسانی: 00:28 02-08-1405)



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
| 1 | `new.lambforkebeb.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.lambforkebeb.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `eyiran1.suser.ir` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=eyiran1.suser.ir&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 3 | `rf.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rf.mishutkin.click&port=443&secret=ee5a994c9e79b5e3ff7ec78e7d7e77eb0b72662e6d69736875746b696e2e636c69636b) |
| 4 | `33.mtprotonewrunningproxasia.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=33.mtprotonewrunningproxasia.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `loud-teal.godserver52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loud-teal.godserver52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 6 | `rade94.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rade94.tidelark.cc&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b7261646539342e746964656c61726b2e6363) |
| 7 | `work.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=work.mishutkin.click&port=443&secret=ee61947a32dca6f584a2772676b4b46924776f726b2e6d69736875746b696e2e636c69636b) |
| 8 | `iranmaster28.suser.ir` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iranmaster28.suser.ir&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 9 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 10 | `194.120.230.106` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.106&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 11 | `dns.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dns.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `0u0006.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=0u0006.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `tokane46.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tokane46.tidelark.cc&port=443&secret=eeae5ab45be1bccbba85eec21085b2fd20746f6b616e6534362e746964656c61726b2e6363) |
| 14 | `41.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=41.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `poka38.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=poka38.tidelark.cc&port=443&secret=eeb0a621aecd97816306c197d21a8bf47b706f6b6133382e746964656c61726b2e6363) |
| 16 | `org.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=org.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `nooshabe.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nooshabe.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 19 | `bfesedv.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bfesedv.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `ir-ir.flipme.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.flipme.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
