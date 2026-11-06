# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:52 15-08-1405)



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
| 1 | `nepo53.foxglade.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nepo53.foxglade.xyz&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b6e65706f35332e666f78676c6164652e78797a) |
| 2 | `speed.runserver.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=speed.runserver.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `im.dumaniltd.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=im.dumaniltd.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `gardeshgar.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gardeshgar.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 5 | `pintrest-cool.browncolor.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pintrest-cool.browncolor.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 6 | `www.torbad.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.torbad.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 7 | `ir-ir.grumpyoldmen.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.grumpyoldmen.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 8 | `nor-bala.flashspder.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nor-bala.flashspder.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 9 | `621.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=621.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `206.71.149.70` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=206.71.149.70&port=8080&secret=vshsJGsgKdnhsKenbsYrbbxhdYsbdb2LanndgsfdhAAAAeee) |
| 11 | `ir.genesbyjohn.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.genesbyjohn.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 12 | `visu82.tidalbirch.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=visu82.tidalbirch.sbs&port=443&secret=eeb8e5365580b9ad3c2ee355dfcbc245e57669737538322e746964616c62697263682e736273) |
| 13 | `ir.sherlock049.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.sherlock049.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 14 | `188.206-197-43.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.206-197-43.ir&port=8443&secret=3RBEBIGHSV36xZoDAiDCXLM) |
| 15 | `kalene97.fernlark.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kalene97.fernlark.xyz&port=8443&secret=eea02849a55daccdc7f7a05691b7ef7cd164726976652e676f6f676c652e636f6d) |
| 16 | `irogallery.golgoli1.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irogallery.golgoli1.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `range-sal.browncolor.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=range-sal.browncolor.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 18 | `comback-all.hosiyaman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=comback-all.hosiyaman.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 19 | `dl.linux-orggv.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dl.linux-orggv.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 20 | `rond-hamrahaval.ebimarh.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rond-hamrahaval.ebimarh.info&port=8443&secret=1603010200010001fc030386e24c3add) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
