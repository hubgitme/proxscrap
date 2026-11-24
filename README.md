# 📊 نتایج استخراج: (آخرین بروزرسانی: 21:01 03-09-1405)



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
| 1 | `usb.neo-duo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=usb.neo-duo.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 2 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 3 | `leomessi.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=leomessi.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `yek.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yek.torob.ir.solzairanbad.ir&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `javar9.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=javar9.ir&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 6 | `haf.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haf.torob.ir.solzairanbad.ir&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `pnj.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `breeze.logmanfi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=breeze.logmanfi.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 9 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `ghasam-be-shab.hosiyaman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ghasam-be-shab.hosiyaman.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 11 | `sun.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sun.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9473756e2e76656c76657477696e646f772e6363) |
| 12 | `vahshianeh.ghodratitarin.info` | `7799` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vahshianeh.ghodratitarin.info&port=7799&secret=dd10400103324995b07c030386e886e7f1) |
| 13 | `caspian-sea.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=caspian-sea.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `noon.begir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noon.begir.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 15 | `support.infinityhalo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=support.infinityhalo.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 16 | `char.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.torob.ir.solzairanbad.ir&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `65.109.250.107` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.250.107&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `you.pelastic.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=you.pelastic.co.uk&port=443&secret=ddc3b375786a3b9630e44cf87d2033a441) |
| 19 | `a3.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a3.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `se.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
