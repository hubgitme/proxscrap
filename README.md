# 📊 نتایج استخراج: (آخرین بروزرسانی: 07:26 04-09-1405)



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
| 1 | `matrixxx.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=matrixxx.vip&port=443&secret=eed0c83b444210a4302be4b1fe17714d4e6d617472697878782e766970) |
| 2 | `freeconnect.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=freeconnect.lol&port=443&secret=eeec15a78c3842e866c302c8526175a68c7975672d6c696e6b2e7275) |
| 3 | `viviri32.kelpmoor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=viviri32.kelpmoor.xyz&port=8443&secret=ee779e9f58a7841578350dfd6d464f46206f7a6f6e2e7275) |
| 4 | `lonezo26.saltfern.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lonezo26.saltfern.xyz&port=8443&secret=eeec569fca8169b57457c573b55bbaa8ec706574726f766963682e7275) |
| 5 | `87.248.144.253` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.253&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 6 | `poneny87.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=poneny87.sorrelbay.xyz&port=8443&secret=eed9f17e3daed2eba291d36ea30d9aded8786170692e6f7a6f6e2e7275) |
| 7 | `gishniz.shambelile.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gishniz.shambelile.co.uk&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 8 | `do.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=do.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 9 | `deny72.ashwren.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=deny72.ashwren.xyz&port=443&secret=eea642c4bcbaceb5aa415464da57a03a37706574726f766963682e7275) |
| 10 | `noh.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noh.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 11 | `www.checker-domain.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.checker-domain.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `ir-countdown.lewisj.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-countdown.lewisj.co.uk&port=8443&secret=104462821249bd7ac519130220c8dd09) |
| 13 | `kite.heronglade.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kite.heronglade.space&port=443&secret=eef34d88320a4d0b6e8aaf11541681dd7c706574726f766963682e7275) |
| 14 | `dastan.sarnevesht.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dastan.sarnevesht.space&port=443&secret=10400103324995b07c030386e886e7f1) |
| 15 | `persian.gulf.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=persian.gulf.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `gardenkite.heronglade.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gardenkite.heronglade.space&port=443&secret=ee4b20619b99880640b45f275c18e20555706574726f766963682e7275) |
| 17 | `dunelumen.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dunelumen.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9464756e656c756d656e2e76656c76657477696e646f772e6363) |
| 18 | `faq.slamawna.info` | `444` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=faq.slamawna.info&port=444&secret=dd41b712fe12019c64e281bcb6aeccded7) |
| 19 | `ultraproxy.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ultraproxy.shop&port=443&secret=eeec15a78c3842e866c302c8526175a68c7975672d6c696e6b2e7275) |
| 20 | `fable.kelpmoor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fable.kelpmoor.xyz&port=8443&secret=ee6fcf868535df2309ee2f6ea5a6563ef9706574726f766963682e7275) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
