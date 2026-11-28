# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:34 07-09-1405)



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
| 1 | `proxy.foriran.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.foriran.co.uk&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 2 | `checker-mizban.dablecheckz.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=checker-mizban.dablecheckz.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 3 | `nice.rozinalpoku.co.uk` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nice.rozinalpoku.co.uk&port=8080&secret=79e344818749bd7ac519130220c25d09) |
| 4 | `citrus.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=citrus.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946369747275732e76656c76657477696e646f772e6363) |
| 5 | `silnet.varfootball.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silnet.varfootball.co.uk&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 6 | `ws24.ir.sam-pars.ir.hamann-motorsports.ir.ip-market.ir.norden-co.com.misaghtalayieh.ir.tiwall.io.saatchi.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ws24.ir.sam-pars.ir.hamann-motorsports.ir.ip-market.ir.norden-co.com.misaghtalayieh.ir.tiwall.io.saatchi.space&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 7 | `ir.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `87.248.144.154` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.154&port=8880&secret=3XnjRIGHSb16xRkTAiDCXQk) |
| 9 | `dune.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dune.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9464756e652e76656c76657477696e646f772e6363) |
| 10 | `ir-ir.mhanna.info` | `3443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.mhanna.info&port=3443&secret=104462821249bd7ac519130220c8dd09) |
| 11 | `loga86.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loga86.sorrelbay.xyz&port=8443&secret=eee38448c7e07ec8d42dfb2ca4d668b790617669746f2e7275) |
| 12 | `91.234.147.18` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.234.147.18&port=443&secret=00000000000000000000000000000000) |
| 13 | `188.245.113.107` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.245.113.107&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `dns.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dns.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `really.azadaiu.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=really.azadaiu.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 16 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `87.248.144.158` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.158&port=8880&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `digi.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.golgoli2.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 19 | `95.216.181.157` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.181.157&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `731.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=731.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
