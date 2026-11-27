# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:01 06-09-1405)



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
  - webproxy, iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn, asr_proxy, proxyskyy, MFDL000

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
| 1 | `yek.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yek.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 3 | `sudosu.appnormoor.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sudosu.appnormoor.info&port=443&secret=dd27729feca8dbcd8008c3fa4f12d92793) |
| 4 | `uncle.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=uncle.telehelp.top&port=443&secret=eed82c6cc1d97c64b7602123fbabd3f537756e636c652e74656c6568656c702e746f70) |
| 5 | `jadid.zhigool.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadid.zhigool.co.uk&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 6 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `dah.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dah.torob.ir.solzairanbad.ir&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `gardenkite.heronglade.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gardenkite.heronglade.space&port=443&secret=ee4b20619b99880640b45f275c18e20555706574726f766963682e7275) |
| 9 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 10 | `77.239.112.39` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.239.112.39&port=443&secret=eea339ca5cc76d3f7946a1356a63f0947d6b69636b2e636f6d) |
| 11 | `ohdox.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ohdox.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `perfect.lavazem3.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=perfect.lavazem3.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 13 | `dunelumen.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dunelumen.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9464756e656c756d656e2e76656c76657477696e646f772e6363) |
| 14 | `95.217.193.214` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.193.214&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 15 | `char.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.anotelinopalk.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 16 | `116.202.246.219` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.202.246.219&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `backups.zangbezanbem.ir` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=backups.zangbezanbem.ir&port=8080&secret=EERighJJvXrFGRMCIMJdCQ) |
| 18 | `lol-lock.godserver52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lol-lock.godserver52.info&port=2020&secret=00000000000000000000000000000000) |
| 19 | `5.222.23.176` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.23.176&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `im.dumaniltd.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=im.dumaniltd.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
