# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:50 01-08-1405)



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
| 1 | `noh.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noh.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `ir.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `ponyny28.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ponyny28.tidelark.cc&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd1706f6e796e7932382e746964656c61726b2e6363) |
| 4 | `tazenafas.dingi3.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tazenafas.dingi3.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `33.antifilterasianew.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=33.antifilterasianew.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `lavashak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lavashak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 7 | `jadide.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadide.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `babak-khoramdin.ir.aysghfkzcxg.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=babak-khoramdin.ir.aysghfkzcxg.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `max.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=max.mishutkin.click&port=443&secret=ee94989d74ad055391384d92c3c773c8d264726976652e676f6f676c652e636f6d) |
| 10 | `joje.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=joje.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `31.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `sumi71.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sumi71.mosswren.vip&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b73756d6937312e6d6f73737772656e2e766970) |
| 13 | `nocloudnew.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nocloudnew.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `7hd78fr.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7hd78fr.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `ir-ir.pbdjarum.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.pbdjarum.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 17 | `91.98.100.233` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.100.233&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `AVA.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AVA.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `65.109.147.34` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.147.34&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 20 | `napoli.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=napoli.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
