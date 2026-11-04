# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:32 13-08-1405)



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
| 1 | `haji-jan.golabkashan.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haji-jan.golabkashan.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 2 | `ir-ir.my-pv.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.my-pv.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `worldmaster.varomax.co.uk` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=worldmaster.varomax.co.uk&port=5500&secret=eeRigzNJvXrFGRMCIMJdEA) |
| 4 | `sn.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sn.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `pnj.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `46.62.224.5` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.62.224.5&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `mofid.saheledarya.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mofid.saheledarya.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `philadelphia.hezarto.info` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=philadelphia.hezarto.info&port=5500&secret=7HQighJPBNMYVRNB6tdkVw) |
| 9 | `petros-es.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=petros-es.co.uk&port=443&secret=ee79e344818749bd7ac519130220c25d09706574726f732d65732e636f2e756b) |
| 10 | `PAyDaR.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=PAyDaR.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `AVA.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AVA.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `mio.foltmeingop.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mio.foltmeingop.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `we.antony-gordon.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=we.antony-gordon.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `strong.hosiyaman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=strong.hosiyaman.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 15 | `white.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=white.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `bo0ji.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bo0ji.co.uk&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 18 | `chd77k7.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chd77k7.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 19 | `new.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `www.shipboard.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.shipboard.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
