# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:50 17-08-1405)



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
| 1 | `s47n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s47n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `dns.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dns.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `www.shipboard.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.shipboard.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 4 | `5ti.do.ru7.lq.v.8v.ir.ir.ir.pd.8kmc.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5ti.do.ru7.lq.v.8v.ir.ir.ir.pd.8kmc.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQAAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 5 | `65.109.147.39` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.147.39&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 6 | `Ay.pj.fon.7g.kp.v.i8.l.1-2-3-4-5.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ay.pj.fon.7g.kp.v.i8.l.1-2-3-4-5.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `soheil.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soheil.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `puot.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=puot.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `ir-ir.connectina.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.connectina.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 10 | `www.basketbalo.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.basketbalo.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 11 | `Pooriyaye-vali.ir.igakwvwa.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Pooriyaye-vali.ir.igakwvwa.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `nice.rozinalpoku.co.uk` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nice.rozinalpoku.co.uk&port=8080&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `Pge.ldi.7g.mk.fs.i.s8.h.kg.37-94-704-33.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Pge.ldi.7g.mk.fs.i.s8.h.kg.37-94-704-33.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `91.98.97.225` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.97.225&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `7r6yjhhk8.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7r6yjhhk8.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `4.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=4.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `comback-all.hosiyaman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=comback-all.hosiyaman.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 18 | `white.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=white.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `195.62.32.55` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.62.32.55&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 20 | `sn.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sn.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
