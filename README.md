# 📊 نتایج استخراج: (آخرین بروزرسانی: 02:11 08-08-1405)



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
| 1 | `77m89.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77m89.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `severjadid.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=severjadid.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `jhndoes.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jhndoes.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `21.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=21.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `craft.malavanann.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=craft.malavanann.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `Fast.finecooking.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fast.finecooking.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 7 | `neka94.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=neka94.tidelark.cc&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd16e656b6139342e746964656c61726b2e6363) |
| 8 | `vasle.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vasle.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `62.238.62.179` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.62.179&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `cocorichmond.pareporeh.info` | `7799` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cocorichmond.pareporeh.info&port=7799&secret=dd10400103324995b07c030386e886e7f1) |
| 11 | `1.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=1.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `loud-teal.godserver52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loud-teal.godserver52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 13 | `core.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=core.proxynet.tech&port=443&secret=ee6963f54d30b8aa1edf4777718f519652636f72652e70726f78796e65742e74656368) |
| 14 | `pnj.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `91.107.171.35` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.171.35&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 16 | `yarypple.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yarypple.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `star.talebi.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=star.talebi.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `ir.speed.finecooking.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.speed.finecooking.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 19 | `nyka85.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nyka85.mosswren.vip&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd16e796b6138352e6d6f73737772656e2e766970) |
| 20 | `ir.xn--ds-bja.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.xn--ds-bja.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
