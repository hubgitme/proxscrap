# 📊 نتایج استخراج: (آخرین بروزرسانی: 03:01 05-09-1405)



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
| 1 | `benze-benz.ir.osahflahyev.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=benze-benz.ir.osahflahyev.info&port=7443&secret=79e344818749bd7ac519130220c25d09) |
| 2 | `noh.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noh.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 3 | `88.99.126.37` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.126.37&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `88.99.211.15` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.211.15&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 5 | `maple.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=maple.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946d61706c652e76656c76657477696e646f772e6363) |
| 6 | `85.133.200.47` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.47&port=8880&secret=dd1603010200010001fc030386e24c3add) |
| 7 | `soh5.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soh5.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `refiq.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=refiq.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 9 | `testt.samanehha.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=testt.samanehha.info&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 10 | `212.118.53.195` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.118.53.195&port=443&secret=dd4482437e89f9af8929514eee7faaf61f) |
| 11 | `name.namenewok.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.namenewok.info&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 12 | `kara.petros-es.co.uk` | `1550` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kara.petros-es.co.uk&port=1550&secret=280597c4f8738458d70e44cbb8b46e8b) |
| 13 | `lonezo26.saltfern.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lonezo26.saltfern.xyz&port=8443&secret=eeec569fca8169b57457c573b55bbaa8ec706574726f766963682e7275) |
| 14 | `ving.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ving.mozitop.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 15 | `dryamusical.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dryamusical.ir&port=443&secret=79e344818749bd7ac519130220c25d09) |
| 16 | `run.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=run.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `ir.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.mediaad.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 18 | `jadide.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadide.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `viny19.kelpmoor.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=viny19.kelpmoor.xyz&port=443&secret=ee71184e2ac505ed5840dd5a00da3318f36f7a6f6e2e7275) |
| 20 | `ir-ir.grumpyoldmen.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.grumpyoldmen.info&port=8443&secret=104462821249bd7ac519130220c8dd09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
