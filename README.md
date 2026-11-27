# 📊 نتایج استخراج: (آخرین بروزرسانی: 19:37 06-09-1405)



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
| 1 | `zonyzo22.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zonyzo22.sorrelbay.xyz&port=8443&secret=ee0a3c55c05f348a0fc2c17b373f9a9157617669746f2e7275) |
| 2 | `netproxystopudovo.duckdns.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=netproxystopudovo.duckdns.org&port=443&secret=eea339ca5cc76d3f7946a1356a63f0947d65626c796174696368746f626c79612e6e6574) |
| 3 | `bimeh.my-moon.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bimeh.my-moon.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `gishniz.shambelile.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gishniz.shambelile.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 5 | `95.111.212.71` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.111.212.71&port=443&secret=ee3db86f433b3aeb5c115185432b0ca1db636c6f7564666c6172652e636f6d) |
| 6 | `quill.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=quill.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c947175696c6c2e7061706572746561706f742e636f6d) |
| 7 | `87.248.144.92` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.92&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `sapphireaurora.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sapphireaurora.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9473617070686972656175726f72612e7061706572746561706f742e636f6d) |
| 9 | `nectar.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nectar.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946e65637461722e7061706572746561706f742e636f6d) |
| 10 | `116.202.246.219` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.202.246.219&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `round.fekr.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=round.fekr.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `91.107.140.144` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.140.144&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 13 | `135.181.74.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.74.183&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 14 | `jadide.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadide.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `company.ferdosisets.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=company.ferdosisets.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 16 | `se.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 17 | `support.infinityhalo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=support.infinityhalo.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `77.239.112.39` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.239.112.39&port=443&secret=eea339ca5cc76d3f7946a1356a63f0947d6b69636b2e636f6d) |
| 19 | `www.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.prxtg.top&port=443&secret=ee4274afdce63c4c3a2b341bad09220a047777772e70727874672e746f70) |
| 20 | `d1.jadroom.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=d1.jadroom.co.uk&port=443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
