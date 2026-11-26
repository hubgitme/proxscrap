# 📊 نتایج استخراج: (آخرین بروزرسانی: 09:01 05-09-1405)



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
| 1 | `s3.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.server-space52.info&port=2020&secret=00000000000000000000000000000000) |
| 2 | `tare.shambelile.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tare.shambelile.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 3 | `ohox.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ohox.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `aurora.velvetoak.work` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aurora.velvetoak.work&port=443&secret=eee418f291b6279b0f441469b2d05e5a7e6c69746536342e73697465) |
| 5 | `craft.malavanann.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=craft.malavanann.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `88.99.126.37` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.126.37&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `fandogh.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fandogh.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `87.248.144.154` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.154&port=8880&secret=dd79e344818749bd7ac519130220c25d09) |
| 9 | `viviri32.kelpmoor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=viviri32.kelpmoor.xyz&port=8443&secret=ee779e9f58a7841578350dfd6d464f46206f7a6f6e2e7275) |
| 10 | `harborwinter.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=harborwinter.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c94686172626f7277696e7465722e7061706572746561706f742e636f6d) |
| 11 | `177.202.67.229` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=177.202.67.229&port=443&secret=ee59e09347d9a61afe7dfaa53d46d55bfd646576656c6f7065722e6e76696469612e636f6d) |
| 12 | `reed.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=reed.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c94726565642e76656c76657477696e646f772e6363) |
| 13 | `hapoo.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hapoo.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 14 | `winter.lavazem2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=winter.lavazem2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `marble.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=marble.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946d6172626c652e7061706572746561706f742e636f6d) |
| 16 | `lilythistle.heronglade.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lilythistle.heronglade.space&port=8443&secret=eef34d88320a4d0b6e8aaf11541681dd7c786170692e6f7a6f6e2e7275) |
| 17 | `server3.esantion.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server3.esantion.info&port=2020&secret=00000000000000000000000000000000) |
| 18 | `sudoaptupdate-y-sudoaptupgrade-y.logmanfi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sudoaptupdate-y-sudoaptupgrade-y.logmanfi.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 19 | `irogallery.golgoli1.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irogallery.golgoli1.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `188.40.68.169` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.40.68.169&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
