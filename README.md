# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:27 23-08-1405)



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
| 1 | `gole-sorati.golabkashan.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gole-sorati.golabkashan.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 2 | `e3fand.fesgheli.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=e3fand.fesgheli.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `194.120.230.37` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.37&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 4 | `www.manazinjamiram.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.manazinjamiram.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 5 | `server93.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server93.server-space52.info&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 6 | `46.225.35.245` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.35.245&port=443&secret=YyEEgYdJXfrFmgMCIMJdjjRueWVrdGFuZXQA) |
| 7 | `star.telbet.lol` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=star.telbet.lol&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `name.namenewok.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.namenewok.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `iran.yes.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iran.yes.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `ir.genesbyjohn.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.genesbyjohn.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 11 | `migato73.foxglade.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=migato73.foxglade.xyz&port=443&secret=eea4a5485d284eb7d8f22ce0fa98c199c9786170692e6f7a6f6e2e7275) |
| 12 | `neka92.larchmere.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=neka92.larchmere.xyz&port=8443&secret=eeb26dd44a039e6125d490c0aeaa262559786170692e6f7a6f6e2e7275) |
| 13 | `195.201.232.21` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.201.232.21&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 14 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `78.47.233.165` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=78.47.233.165&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `baran.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=baran.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `worldmaster.varomax.co.uk` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=worldmaster.varomax.co.uk&port=5500&secret=eeRigzNJvXrFGRMCIMJdEA) |
| 18 | `haji-jan.golabkashan.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haji-jan.golabkashan.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 19 | `vima78.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vima78.tidelark.cc&port=443&secret=eeb0a621aecd97816306c197d21a8bf47b76696d6137382e746964656c61726b2e6363) |
| 20 | `Speed-speed.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Speed-speed.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
