# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:53 24-08-1405)



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
| 1 | `PAyDaR.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=PAyDaR.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `9f.do.s.or.6j8.so.r.torbad.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=9f.do.s.or.6j8.so.r.torbad.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `bastani.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bastani.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 4 | `9ohdjo.me.7f.ckl.a3.h.172-63.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=9ohdjo.me.7f.ckl.a3.h.172-63.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `t4.myrka.digital` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=t4.myrka.digital&port=443&secret=ee1111222233334444555566667777888874342e6d79726b612e6469676974616c) |
| 6 | `He.le.y9.bst.xo.t.72-403-837-543.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=He.le.y9.bst.xo.t.72-403-837-543.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `176.65.128.63` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.65.128.63&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 8 | `7r6yjhhk8.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7r6yjhhk8.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `gishniz.shambelile.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gishniz.shambelile.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 10 | `88.99.126.37` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.126.37&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `91.98.219.255` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.219.255&port=8443&secret=dd5f7ce28a2c4816c6c923dfd4d5630e01dd) |
| 12 | `ir.sherlock049.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.sherlock049.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 13 | `srv-xexobc.mtshop.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=srv-xexobc.mtshop.xyz&port=443&secret=eeabe97898bfc981fc5a8a20f5953f08ac646c2e676f6f676c652e636f6d) |
| 14 | `new.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `irogallery.golgoli1.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irogallery.golgoli1.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `hamrah.coudflare.ww.qavi-13.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hamrah.coudflare.ww.qavi-13.co.uk&port=8443&secret=7l984oosSBbGySPf1NVjDgE=) |
| 17 | `88.99.125.56` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.125.56&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `misu42.copperwren.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=misu42.copperwren.click&port=443&secret=eebeb3cc6e60d47ebe83eccee3c0475a47786170692e6f7a6f6e2e7275) |
| 19 | `irluxcars.site` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irluxcars.site&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `cdn1.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn1.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
