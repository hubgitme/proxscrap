# 📊 نتایج استخراج: (آخرین بروزرسانی: 05:02 05-09-1405)



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
| 1 | `day.lavazem4.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=day.lavazem4.co.uk&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 2 | `exiscos.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=exiscos.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 3 | `shish.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shish.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 4 | `harborwinter.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=harborwinter.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c94686172626f7277696e7465722e7061706572746561706f742e636f6d) |
| 5 | `95.111.214.0` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.111.214.0&port=443&secret=ee89b6f6c9fd067a955fd12ca4c158ec00636c6f7564666c6172652e636f6d) |
| 6 | `17fh.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=17fh.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `jadid.porsorate.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadid.porsorate.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `violet.ashwren.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=violet.ashwren.xyz&port=443&secret=ee6fcf868535df2309ee2f6ea5a6563ef962726f777365722e79616e6465782e7275) |
| 9 | `live.lovely.lat` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=live.lovely.lat&port=443&secret=eeaadd88aa9facd454936d0c42dc128e776c6976652e6c6f76656c792e6c6174) |
| 10 | `loga86.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loga86.sorrelbay.xyz&port=8443&secret=eee38448c7e07ec8d42dfb2ca4d668b790617669746f2e7275) |
| 11 | `great.cipservice.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=great.cipservice.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `russia.knox-proxy.world` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=russia.knox-proxy.world&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `winter.lavazem2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=winter.lavazem2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `faq.slamawna.info` | `444` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=faq.slamawna.info&port=444&secret=dd41b712fe12019c64e281bcb6aeccded7) |
| 15 | `perfect.lavazem3.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=perfect.lavazem3.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 16 | `zone88.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zone88.sorrelbay.xyz&port=8443&secret=ee0a717e9ba394eff63a9943ff11493cc2706574726f766963682e7275) |
| 17 | `char.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.anotelinopalk.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 18 | `116.202.246.219` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.202.246.219&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `quill.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=quill.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c947175696c6c2e7061706572746561706f742e636f6d) |
| 20 | `azadi.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=azadi.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
