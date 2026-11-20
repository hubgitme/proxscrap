# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:24 29-08-1405)



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
  - webproxy, iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn, asr_proxy, proxyskyy

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
| 1 | `135.181.74.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.74.189&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 2 | `dunelumen.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dunelumen.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9464756e656c756d656e2e76656c76657477696e646f772e6363) |
| 3 | `3etare.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3etare.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `Suodbo.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Suodbo.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 5 | `s47n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s47n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `solar.heronglade.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=solar.heronglade.space&port=443&secret=ee4b20619b99880640b45f275c18e20555706574726f766963682e7275) |
| 7 | `felan-by.lolauth.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=felan-by.lolauth.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 8 | `iro.varfootball2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iro.varfootball2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `a2.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a2.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `craft.malavanann.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=craft.malavanann.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `194.120.230.106` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.106&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 12 | `65.109.106.179` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.106.179&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 13 | `neon.tealbriar.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=neon.tealbriar.xyz&port=8443&secret=ee7809adb838f02953d8f53df91d2e4b35706574726f766963682e7275) |
| 14 | `gshs7o.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gshs7o.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `fame.saalaad.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fame.saalaad.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `naznazi.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=naznazi.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `a3.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a3.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `H2O.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=H2O.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 19 | `hamishe.hastim.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hamishe.hastim.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 20 | `195.18.10.204` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.18.10.204&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
