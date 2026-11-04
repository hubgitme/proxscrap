# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:57 13-08-1405)



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
| 1 | `178.105.123.147` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.123.147&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQAAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 2 | `lezoka78.quillmarsh.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lezoka78.quillmarsh.xyz&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e6c657a6f6b6137382e7175696c6c6d617273682e78797a) |
| 3 | `exiscos.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=exiscos.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `prime.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prime.proxynet.tech&port=443&secret=ee6462eda0da18f27d4ecbac590aa970a07072696d652e70726f78796e65742e74656368) |
| 5 | `top.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=top.proxynet.tech&port=443&secret=ee59d1ef95ab03cfeaebb18b0a529ad5e6746f702e70726f78796e65742e74656368) |
| 6 | `irluxcars.site` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irluxcars.site&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `aseman.lunavane.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aseman.lunavane.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `isna.ir.asriran.com.varzesh3.com.yalandonyi.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=isna.ir.asriran.com.varzesh3.com.yalandonyi.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `legato86.quietfjord.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=legato86.quietfjord.click&port=443&secret=eeae5ab45be1bccbba85eec21085b2fd206c656761746f38362e7175696574666a6f72642e636c69636b) |
| 10 | `zebedeh.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zebedeh.ir&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `pintrest-cool.browncolor.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pintrest-cool.browncolor.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 12 | `www.manazinjamiram.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.manazinjamiram.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 13 | `petros-es.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=petros-es.co.uk&port=443&secret=ee79e344818749bd7ac519130220c25d09706574726f732d65732e636f2e756b) |
| 14 | `195.18.10.204` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.18.10.204&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |
| 15 | `vahshianeh.ghodratitarin.info` | `7799` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vahshianeh.ghodratitarin.info&port=7799&secret=dd10400103324995b07c030386e886e7f1) |
| 16 | `521.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=521.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `nigan.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nigan.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `ir.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `194.120.230.120` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.120&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 20 | `pofak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pofak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
