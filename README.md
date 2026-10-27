# 📊 نتایج استخراج: (آخرین بروزرسانی: 18:37 05-08-1405)



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
| 1 | `darya.saheledarya.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=darya.saheledarya.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `91.107.171.35` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.171.35&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 3 | `napoli.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=napoli.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 5 | `65.109.147.39` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.147.39&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 6 | `Magic.godserver52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Magic.godserver52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 7 | `ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 8 | `like.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=like.mishutkin.click&port=443&secret=eeb5564aa26504e3e4f43d5fbd43c24abc6c696b652e6d69736875746b696e2e636c69636b) |
| 9 | `ir.lv223.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.lv223.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 10 | `195.18.10.204` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.18.10.204&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |
| 11 | `ccc.horizon555.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ccc.horizon555.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `62.238.62.179` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.62.179&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `philadelphia.hezarto.info` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=philadelphia.hezarto.info&port=5500&secret=7HQighJPBNMYVRNB6tdkVw) |
| 14 | `731.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=731.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `34.87.158.150` | `12432` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=34.87.158.150&port=12432&secret=eeeaabea0b96a8e55f0f842afd282417d07777772e6d6963726f736f66742e636f6d) |
| 16 | `sukari30.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sukari30.tidelark.cc&port=443&secret=ee14697011e0c73f03e95d7b6919a2252b73756b61726933302e746964656c61726b2e6363) |
| 17 | `digi.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `bo0ji.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bo0ji.co.uk&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 19 | `Pasargad.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Pasargad.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `AZADI.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AZADI.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
