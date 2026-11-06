# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:22 15-08-1405)



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
| 1 | `178.105.137.152` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.137.152&port=443&secret=eeabf13064a3bf0851a02ad67114f842ce676f6f676c65617069732e636f6d) |
| 2 | `new.nakoskoskesh.co.uk` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.nakoskoskesh.co.uk&port=8080&secret=EERighJJvXrFGRMCIMJdCQ) |
| 3 | `srv-jxcxnq.gomt.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=srv-jxcxnq.gomt.shop&port=443&secret=ee159371b5cc81b0fd73f8aa7e13e2346d646c2e676f6f676c652e636f6d) |
| 4 | `panir.begir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panir.begir.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 5 | `bo0ji.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bo0ji.co.uk&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 6 | `strong.hosiyaman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=strong.hosiyaman.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 7 | `range-sal.browncolor.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=range-sal.browncolor.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 8 | `support.infinityhalo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=support.infinityhalo.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `pashmak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pashmak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 10 | `ir-ir.naganuma.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.naganuma.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 11 | `195.62.32.55` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.62.32.55&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 12 | `mirima84.copperwren.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mirima84.copperwren.click&port=443&secret=ee9267d78681726d5ff1bf826b750ba4ba6d6972696d6138342e636f707065727772656e2e636c69636b) |
| 13 | `77.216.4.149` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.216.4.149&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 14 | `rad.irani-pr.net` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rad.irani-pr.net&port=85&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `dizgrakh.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dizgrakh.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `good.cipservice.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=good.cipservice.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `tolera44.copperwren.click` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tolera44.copperwren.click&port=8443&secret=ee24c8636b7e946779a023ee708370719b64726976652e676f6f676c652e636f6d) |
| 18 | `max.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=max.mishutkin.click&port=443&secret=ee94989d74ad055391384d92c3c773c8d264726976652e676f6f676c652e636f6d) |
| 19 | `169.58.86.18` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=169.58.86.18&port=443&secret=ee85dc3d6c2900e59b6f97f68ee7d1e349676f6f676c65617069732e636f6d) |
| 20 | `ir.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
