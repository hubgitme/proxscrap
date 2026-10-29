# 📊 نتایج استخراج: (آخرین بروزرسانی: 12:49 07-08-1405)



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
| 1 | `f123.e7.yayayajd.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=f123.e7.yayayajd.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `cdn1.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn1.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `Rudmoain.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Rudmoain.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 4 | `www.yesyesno.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.yesyesno.ir&port=8443&secret=3RcBGGq9DqYBIxkuJkNPkaU) |
| 5 | `ir.forzajuve.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.forzajuve.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 6 | `bastani.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bastani.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 7 | `leomessi.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=leomessi.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `AZADI.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AZADI.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `prime.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prime.proxynet.tech&port=443&secret=ee6462eda0da18f27d4ecbac590aa970a07072696d652e70726f78796e65742e74656368) |
| 10 | `dokhtar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dokhtar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 11 | `ir-ir.simpleelegance-us.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.simpleelegance-us.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 12 | `digi.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `web.mangoseason7.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.mangoseason7.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `qadim.zhigool.co.uk` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=qadim.zhigool.co.uk&port=22&secret=EERighJJvXrFGRMCIMJdCQ) |
| 15 | `silnet.varfootball.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silnet.varfootball.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `char.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `irluxcars.site` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irluxcars.site&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `cdn1.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn1.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `ir-ir.flipme.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.flipme.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 20 | `ir-ir.rebol.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.rebol.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
