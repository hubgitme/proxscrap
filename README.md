# 📊 نتایج استخراج: (آخرین بروزرسانی: 21:01 06-09-1405)



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
| 1 | `2y.kr.8v.lr.f.ir.75.44.38-82.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2y.kr.8v.lr.f.ir.75.44.38-82.ir&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 2 | `maraka16.ashwren.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=maraka16.ashwren.xyz&port=443&secret=ee912defad667a620d66dbf5fd0b2a1bcc62726f777365722e79616e6465782e7275) |
| 3 | `3etare.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3etare.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 4 | `95.111.215.100` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.111.215.100&port=443&secret=ee74f6feeccaba4ced3c2057328addd5b6636c6f7564666c6172652e636f6d) |
| 5 | `5.222.17.103` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.17.103&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `round.fekr.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=round.fekr.co.uk&port=2083&secret=79e344818749bd7ac519130220c25d09) |
| 7 | `man-to-man.dablecheckz.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=man-to-man.dablecheckz.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 8 | `79.137.196.223` | `21443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=21443&secret=ee70d02df07ecb5669b6eb010aba55eab07777772e636c6f7564666c6172652e636f6d) |
| 9 | `cdn.divpal.com` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn.divpal.com&port=8443&secret=dd71889eb517157210d61df330a5f11d95) |
| 10 | `termsnal.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=termsnal.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 11 | `79.137.196.223` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=8443&secret=eeeeacd334a255675ccc880cb6b8c9caf07777772e636c6f7564666c6172652e636f6d) |
| 12 | `iro.varfootball2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iro.varfootball2.co.uk&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 13 | `o0hd9opx.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=o0hd9opx.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `91.107.155.20` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.155.20&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `s3.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.server-space52.info&port=2020&secret=00000000000000000000000000000000) |
| 16 | `87.248.144.155` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.155&port=8880&secret=dd1603010200010001fc030386e24c3add) |
| 17 | `95.111.212.44` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.111.212.44&port=443&secret=ee37d89185cc2c0d277a5506e5f18325b1636c6f7564666c6172652e636f6d) |
| 18 | `85.133.200.45` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.45&port=8880&secret=3RYDAQIAAQAB_AMDhuJMOt0) |
| 19 | `zone88.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zone88.sorrelbay.xyz&port=8443&secret=ee0a717e9ba394eff63a9943ff11493cc2706574726f766963682e7275) |
| 20 | `this-is.fastnet-vpn.xyz` | `4443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=this-is.fastnet-vpn.xyz&port=4443&secret=ee466f3ef394f7c682a47b604deda898ea746869732d69732e666173746e65742d76706e2e78797a) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
