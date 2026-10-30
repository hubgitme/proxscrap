# 📊 نتایج استخراج: (آخرین بروزرسانی: 07:49 08-08-1405)



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
| 1 | `panir.begir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panir.begir.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 2 | `pnj.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `Suodbo.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Suodbo.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 4 | `fast.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.mishutkin.click&port=443&secret=eef767ebee5708dadc985d58ad6e04560664726976652e676f6f676c652e636f6d) |
| 5 | `hadaf.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hadaf.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `din5gli2.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=din5gli2.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `aparat.com.filimo.com.namava.ir.telewebion.com.ghoostbusters.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aparat.com.filimo.com.namava.ir.telewebion.com.ghoostbusters.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `maka61.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=maka61.tidelark.cc&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e6d616b6136312e746964656c61726b2e6363) |
| 9 | `ir-ir.rebol.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.rebol.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 10 | `for.you.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=for.you.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 12 | `ir-ir.radio-zvez.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.radio-zvez.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 13 | `mio.foltmeingop.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mio.foltmeingop.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `46.225.148.183` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.148.183&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `tassian.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tassian.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `petros-es.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=petros-es.co.uk&port=443&secret=ee79e344818749bd7ac519130220c25d09706574726f732d65732e636f2e756b) |
| 17 | `dizgrakh.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dizgrakh.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `kostyanchekloh.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kostyanchekloh.lol&port=443&secret=ee3f72634c46d320aaa30d8bb2682e9b497975672d6c696e6b2e7275) |
| 19 | `shoes.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shoes.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `521.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=521.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
