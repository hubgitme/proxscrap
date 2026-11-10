# 📊 نتایج استخراج: (آخرین بروزرسانی: 09:24 19-08-1405)



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
| 1 | `new.nakoskoskesh.co.uk` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.nakoskoskesh.co.uk&port=8080&secret=EERighJJvXrFGRMCIMJdCQ) |
| 2 | `ir.lv223.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.lv223.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `88.99.126.37` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.126.37&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `snapp.ir.neshan.org.tapsi.ir.balad.ir.siyahsefidi.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=snapp.ir.neshan.org.tapsi.ir.balad.ir.siyahsefidi.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `5.42.114.210` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.42.114.210&port=443&secret=ee853c6d9722a3789f8533cd9dd0baec1b7777772e617669746f2e7275) |
| 6 | `194.120.230.120` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.120&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 7 | `digi.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `185.166.214.158` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.166.214.158&port=8443&secret=7n3yZ_5IshU33VFu-RJW7fZ3d3cuYXBwbGUuY29t) |
| 9 | `dizgrakh.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dizgrakh.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `xxmatrixx.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=xxmatrixx.top&port=853&secret=eee4508d288bf81791177a2f5e73ac06cf6d617472697878782e746f70) |
| 11 | `pesar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pesar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 12 | `pomide92.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pomide92.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e706f6d69646539322e6d6f73737772656e2e766970) |
| 13 | `178.105.137.152` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.137.152&port=443&secret=eeabf13064a3bf0851a02ad67114f842ce676f6f676c65617069732e636f6d) |
| 14 | `ir-ir.my-pv.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.my-pv.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 15 | `puot.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=puot.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `we.antony-gordon.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=we.antony-gordon.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `vasalshim.mamadgoli.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vasalshim.mamadgoli.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `6h.do.i.d5.dk.7f.36-94-77-3.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6h.do.i.d5.dk.7f.36-94-77-3.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `friable.honing.jaunty.misuser.pizzazz.pinoyteleseryerewind.org` | `5350` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=friable.honing.jaunty.misuser.pizzazz.pinoyteleseryerewind.org&port=5350&secret=ee629eaf63a95797db098e53fc654812a373332e616d617a6f6e6177732e636f6d) |
| 20 | `ir-ir.goaphrodite.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.goaphrodite.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
