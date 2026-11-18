# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:27 27-08-1405)



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
| 1 | `partnerupload.steampower.online` | `3864` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=partnerupload.steampower.online&port=3864&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `194.120.230.26` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.26&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 3 | `ghasam-be-shab.hosiyaman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ghasam-be-shab.hosiyaman.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 4 | `188.34.192.90` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.34.192.90&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==) |
| 5 | `white.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=white.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `ir.philgent.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.philgent.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 7 | `my.soft98.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=my.soft98.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `jadid.porsorate.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadid.porsorate.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `Gos.8f.dk.euv.4h.d.kw.68-309-27-46.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Gos.8f.dk.euv.4h.d.kw.68-309-27-46.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `91.98.109.248` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.109.248&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `www.servertala.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.servertala.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 12 | `dh1.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dh1.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `nocloudnew.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nocloudnew.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `ir.lv223.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.lv223.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 16 | `dizgrakh.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dizgrakh.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `pintrest-cool.browncolor.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pintrest-cool.browncolor.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 18 | `z.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=z.prxtg.top&port=443&secret=ee7e17a7ab0683c8c697302c61363d5e957a2e70727874672e746f70) |
| 19 | `ir.strobox.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.strobox.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 20 | `ir.xn--ds-bja.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.xn--ds-bja.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
