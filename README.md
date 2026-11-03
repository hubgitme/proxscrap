# 📊 نتایج استخراج: (آخرین بروزرسانی: 17:07 12-08-1405)



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
| 1 | `mashti.setado.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mashti.setado.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `Dho.phd.iv.md.h.g.if.7.www1www.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Dho.phd.iv.md.h.g.if.7.www1www.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `irogallery.golgoli1.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irogallery.golgoli1.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `ir.barhousefarm.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.barhousefarm.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 5 | `46.62.220.216` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.62.220.216&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `Suodbo.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Suodbo.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 7 | `ir-ir.grumpyoldmen.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.grumpyoldmen.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 8 | `tolo60.fernlark.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tolo60.fernlark.xyz&port=443&secret=ee920a4026fcc79354d87c30db9280e578746f6c6f36302e6665726e6c61726b2e78797a) |
| 9 | `shsh.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shsh.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `17fh.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=17fh.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `haf.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haf.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `mio.miosen.cyou` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mio.miosen.cyou&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `se.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `server1.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server1.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 15 | `91.98.107.89` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.107.89&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `premium.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `ir.panhandleflyers.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.panhandleflyers.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 18 | `333.mtprotonewrunningproxasia.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=333.mtprotonewrunningproxasia.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `soh5.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soh5.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `ir-ir.engematica.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.engematica.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
