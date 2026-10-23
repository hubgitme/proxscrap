# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:29 01-08-1405)



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
| 1 | `mide77.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mide77.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e6d69646537372e6d6f73737772656e2e766970) |
| 2 | `65.109.147.34` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.147.34&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 3 | `kasco.alhosein.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kasco.alhosein.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `bookmook.hichibehichi-co.info` | `2882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bookmook.hichibehichi-co.info&port=2882&secret=dd10400103324995b07c030386e886e7f1) |
| 5 | `isaco.ir.setado.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=isaco.ir.setado.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `for.you.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=for.you.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `milann.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=milann.ir&port=8443&secret=dd79e344818749bd7ac519130220c25d09) |
| 8 | `mio.foltmeingop.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mio.foltmeingop.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `ir.lv223.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.lv223.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 10 | `rf.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rf.mishutkin.click&port=443&secret=ee5a994c9e79b5e3ff7ec78e7d7e77eb0b72662e6d69736875746b696e2e636c69636b) |
| 11 | `uwu.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=uwu.mishutkin.click&port=443&secret=eec21a6ac829a6acfe1077910fc3da1c127577752e6d69736875746b696e2e636c69636b) |
| 12 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `ir-ir.ariely.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.ariely.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 14 | `135.181.154.26` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.154.26&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `pashmak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pashmak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 16 | `recordzan.herfeibash.info` | `7799` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=recordzan.herfeibash.info&port=7799&secret=dd10400103324995b07c030386e886e7f1) |
| 17 | `204.168.207.138` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.207.138&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `ir-ir.engematica.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.engematica.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 19 | `ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 20 | `hadaf.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hadaf.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
