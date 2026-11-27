# 📊 نتایج استخراج: (آخرین بروزرسانی: 03:01 07-09-1405)



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
| 1 | `87.248.144.60` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.60&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `5.222.20.63` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.20.63&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `shahname.ferdosisets.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shahname.ferdosisets.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 4 | `79.137.196.223` | `4443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=4443&secret=eeee4026e99e99216664b0cb156da676d7707777772e636c6f7564666c6172652e636f6d) |
| 5 | `dele89.quillmarsh.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dele89.quillmarsh.xyz&port=8443&secret=ee704c9352bad79b00f1e067772277715664726976652e676f6f676c652e636f6d) |
| 6 | `pine.heronglade.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pine.heronglade.space&port=8443&secret=ee4b20619b99880640b45f275c18e20555786170692e6f7a6f6e2e7275) |
| 7 | `shoes.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shoes.golgoli2.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 8 | `87.248.144.167` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.167&port=8880&secret=3RYDAQIAAQAB_AMDhuJMOt0) |
| 9 | `daryapiano.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=daryapiano.ir&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 10 | `ir-immortals.sponsorafuture.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-immortals.sponsorafuture.co.uk&port=443&secret=104462821249bd7ac519130220c8dd09) |
| 11 | `sudoaptupdate-y-sudoaptupgrade-y.logmanfi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sudoaptupdate-y-sudoaptupgrade-y.logmanfi.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 12 | `178.104.214.47` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.214.47&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `21.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=21.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `pesar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pesar.nanaz.co.uk&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 15 | `fruit.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fruit.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `scofield.iaubpanel.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=scofield.iaubpanel.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 17 | `from.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=from.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `soh5.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soh5.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `payer.dablecheckz.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=payer.dablecheckz.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 20 | `soheil.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soheil.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
