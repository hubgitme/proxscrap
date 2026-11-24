# 📊 نتایج استخراج: (آخرین بروزرسانی: 03:01 04-09-1405)



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
| 1 | `tazenafas.dingi3.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tazenafas.dingi3.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `javar10.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=javar10.ir&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 3 | `foxfrost.heronglade.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=foxfrost.heronglade.space&port=8443&secret=eef34d88320a4d0b6e8aaf11541681dd7c786170692e6f7a6f6e2e7275) |
| 4 | `viny19.kelpmoor.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=viny19.kelpmoor.xyz&port=443&secret=ee71184e2ac505ed5840dd5a00da3318f36f7a6f6e2e7275) |
| 5 | `83.243.86.176` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=83.243.86.176&port=7443&secret=79e344818749bd7ac519130220c25d09) |
| 6 | `s7n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s7n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `85.133.200.41` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.41&port=8880&secret=dd79e344818749bd7ac519130220c25d09) |
| 8 | `tebarad.ir` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tebarad.ir&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `top.fastprx.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=top.fastprx.top&port=443&secret=ee2eaa3efe26957df17447871a78aa19b064726976652e676f6f676c652e636f6d) |
| 10 | `156.229.167.222` | `5201` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=156.229.167.222&port=5201&secret=ee3a51554a1c8542cc36572fd59c2f63f4617a7572652e6d6963726f736f66742e636f6d) |
| 11 | `loga86.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loga86.sorrelbay.xyz&port=8443&secret=eee38448c7e07ec8d42dfb2ca4d668b790617669746f2e7275) |
| 12 | `benze-benz.ir.osahflahyev.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=benze-benz.ir.osahflahyev.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `day.lavazem4.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=day.lavazem4.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `pnj.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.ionox.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `yek.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yek.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `51.hide.7y76y.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=51.hide.7y76y.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `darkdept.store` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=darkdept.store&port=8443&secret=ee4cdc677c2048afa846136f4a70c05e827777772e6461726b646570742e73746f7265) |
| 18 | `a1.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a1.anotelinopalk.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 19 | `irogallery.golgoli1.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irogallery.golgoli1.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `21.hide.7y76y.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=21.hide.7y76y.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
