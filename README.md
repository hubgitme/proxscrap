# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:23 05-09-1405)



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
| 1 | `91.234.147.18` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.234.147.18&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 2 | `banoo.khooorshid.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=banoo.khooorshid.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `rond-hamrahaval.ebimarh.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rond-hamrahaval.ebimarh.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 4 | `87.248.144.249` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.249&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 5 | `s7n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s7n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `as.mkim.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=as.mkim.click&port=443&secret=ee2dfa3526fc70b7abd7a09eade6ccea1f61732e6d6b696d2e636c69636b) |
| 7 | `87.248.144.249` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.249&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `65.109.191.110` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.191.110&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 9 | `85.133.200.13` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.13&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 10 | `hasht.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hasht.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 11 | `gram.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gram.proxynet.tech&port=443&secret=ee46a30f9e2a6c81ba8466e5055d3d497a64726976652e676f6f676c652e636f6d) |
| 12 | `tg.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.prxtg.top&port=443&secret=ee2d1bb45f31056d1063563fc6e38e5a1064726976652e676f6f676c652e636f6d) |
| 13 | `ghasam-be-shab.hosiyaman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ghasam-be-shab.hosiyaman.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 14 | `212.108.98.5` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.108.98.5&port=443&secret=dd1603010200010001fc030386e24c3add) |
| 15 | `ccc.horizon555.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ccc.horizon555.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 16 | `mile20.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mile20.sorrelbay.xyz&port=8443&secret=eee1d528d13649f8288c1ea7898787b486786170692e6f7a6f6e2e7275) |
| 17 | `ving.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ving.mozitop.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 18 | `raleto69.fernlark.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=raleto69.fernlark.xyz&port=443&secret=ee8ac4f89d6036e07f6ff9e00b1699819e706574726f766963682e7275) |
| 19 | `79.137.196.223` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=2053&secret=eeee1701dff011da0ee1313d584fc565187777772e636c6f7564666c6172652e636f6d) |
| 20 | `s2.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s2.server-space52.info&port=2020&secret=00000000000000000000000000000000) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
