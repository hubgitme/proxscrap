# 📊 نتایج استخراج: (آخرین بروزرسانی: 03:44 11-08-1405)



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
| 1 | `nfc.neo-duo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nfc.neo-duo.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 2 | `sn.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sn.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `hibf6.ir.lpfss.co.uk.i9l9.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hibf6.ir.lpfss.co.uk.i9l9.ir&port=8443&secret=7hYDAQIAAQAB_AMEhuJMOt0) |
| 4 | `ir.barhousefarm.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.barhousefarm.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 5 | `dizgrakh.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dizgrakh.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `isaco.ir.setado.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=isaco.ir.setado.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `ir-ir.simpleelegance-us.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.simpleelegance-us.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 8 | `iro.varfootball2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iro.varfootball2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `luxuryman.sbs` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=luxuryman.sbs&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `Fast.finecooking.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fast.finecooking.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 11 | `hash.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hash.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `mangoseason8.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mangoseason8.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `web.mangoseason7.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.mangoseason7.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `www.jodaeimanam.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.jodaeimanam.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 15 | `petros-es.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=petros-es.co.uk&port=443&secret=ee79e344818749bd7ac519130220c25d09706574726f732d65732e636f2e756b) |
| 16 | `royaclinic.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=royaclinic.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `s3.soft98.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.soft98.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `www.setado.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.setado.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 19 | `MAP.cooptoop.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=MAP.cooptoop.site&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 20 | `leomessi.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=leomessi.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
