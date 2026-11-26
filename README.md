# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:01 05-09-1405)



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
| 1 | `termsnal.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=termsnal.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 2 | `exiscos.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=exiscos.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `ir-countdown.lewisj.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-countdown.lewisj.co.uk&port=8443&secret=104462821249bd7ac519130220c8dd09) |
| 4 | `91.234.147.28` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.234.147.28&port=443&secret=00000000000000000000000000000000) |
| 5 | `vinyga35.quillmarsh.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vinyga35.quillmarsh.xyz&port=8443&secret=ee66209693c31923590235bff3baec4bc164726976652e676f6f676c652e636f6d) |
| 6 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `91.107.155.20` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.155.20&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `quill.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=quill.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c947175696c6c2e7061706572746561706f742e636f6d) |
| 9 | `noh.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noh.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `65.109.176.207` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.176.207&port=8443&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `79.137.196.223` | `15443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=15443&secret=ee5d739d0cab70b86961816e3a9c27d4c17777772e636c6f7564666c6172652e636f6d) |
| 12 | `o05d9opx.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=o05d9opx.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `ohox.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ohox.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `mamadgoli.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mamadgoli.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `jy7nf.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jy7nf.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 16 | `dash.linux-orggv.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dash.linux-orggv.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `jhndoes.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jhndoes.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `noh.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noh.torob.ir.solzairanbad.ir&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 19 | `65.109.210.26` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.210.26&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 20 | `ir-immortals.sponsorafuture.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-immortals.sponsorafuture.co.uk&port=443&secret=104462821249bd7ac519130220c8dd09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
