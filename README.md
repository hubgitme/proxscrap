# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:38 30-07-1405)



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
| 1 | `u8886h6.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=u8886h6.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `foc.pf.og.mro.7f.j7.spb.f.lwww.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=foc.pf.og.mro.7f.j7.spb.f.lwww.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `Dho.phd.iv.md.h.g.if.7.www1www.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Dho.phd.iv.md.h.g.if.7.www1www.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `haji.estabonita.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haji.estabonita.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 5 | `nano.ninjatool9.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nano.ninjatool9.ir&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 6 | `rf.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rf.mishutkin.click&port=443&secret=ee5a994c9e79b5e3ff7ec78e7d7e77eb0b72662e6d69736875746b696e2e636c69636b) |
| 7 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 8 | `mimizo19.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mimizo19.tidelark.cc&port=443&secret=ee6ce7aa9636179a5f67366aaab4702a266d696d697a6f31392e746964656c61726b2e6363) |
| 9 | `tassian.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tassian.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `premium.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `redflag.yazaebalsyadelatproxy.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.vip&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd1726564666c61672e79617a616562616c73796164656c617470726f78792e766970) |
| 12 | `panel.hook--tehran.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panel.hook--tehran.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 13 | `t5.nevcodeframe.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=t5.nevcodeframe.com&port=443&secret=ee4e7e658f96af22ada977fa3e2e472e6274352e6e6576636f64656672616d652e636f6d) |
| 14 | `tokane46.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tokane46.tidelark.cc&port=443&secret=eeae5ab45be1bccbba85eec21085b2fd20746f6b616e6534362e746964656c61726b2e6363) |
| 15 | `Lashboy.muzanesghy.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Lashboy.muzanesghy.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `nasho.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nasho.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `run.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=run.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `ir.flipme.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.flipme.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 19 | `web.mangoseason7.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.mangoseason7.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `irluxcars.site` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irluxcars.site&port=4455&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
