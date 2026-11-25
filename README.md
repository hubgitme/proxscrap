# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:01 04-09-1405)



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
| 1 | `188.40.68.147` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.40.68.147&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 2 | `65.109.98.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.98.231&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 3 | `max.kimt.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=max.kimt.click&port=443&secret=ee1b153cf06dbd43c6085c359a6702eb936d61782e6b696d742e636c69636b) |
| 4 | `85.133.200.12` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.12&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 5 | `do.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=do.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 6 | `172.245.219.148` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.245.219.148&port=443&secret=ee00000000000000000000000000000000636c6f7564666c6172652e636f6d) |
| 7 | `91.98.102.82` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.102.82&port=8443&secret=1603010200010001fc030386e24c3add) |
| 8 | `live.lovely.lat` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=live.lovely.lat&port=443&secret=eeaadd88aa9facd454936d0c42dc128e776c6976652e6c6f76656c792e6c6174) |
| 9 | `ir-neverland.nowhearthis.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-neverland.nowhearthis.co.uk&port=8443&secret=104462821249bd7ac519130220c8dd09) |
| 10 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `winter.lavazem2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=winter.lavazem2.co.uk&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 12 | `bukk.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bukk.ir&port=8443&secret=dd79e344818749bd7ac519130220c25d09) |
| 13 | `j7nf.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=j7nf.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 14 | `loga86.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loga86.sorrelbay.xyz&port=8443&secret=eee38448c7e07ec8d42dfb2ca4d668b790617669746f2e7275) |
| 15 | `wbs.regmail.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=wbs.regmail.org&port=443&secret=ee5610dcb9c93a1c5dd38d965b0462ad2c7762732e7265676d61696c2e6f7267) |
| 16 | `tg.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.prxtg.top&port=443&secret=ee2d1bb45f31056d1063563fc6e38e5a1064726976652e676f6f676c652e636f6d) |
| 17 | `94.130.94.122` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.130.94.122&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 18 | `85.133.200.45` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.45&port=8880&secret=dd1603010200010001fc030386e24c3add) |
| 19 | `61.hide.7y76y.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=61.hide.7y76y.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `91.98.223.136` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.223.136&port=8443&secret=1603010200010001fc030386e24c3add) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
