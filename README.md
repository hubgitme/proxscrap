# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:48 04-08-1405)



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
| 1 | `raga84.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=raga84.mosswren.vip&port=443&secret=ee920a4026fcc79354d87c30db9280e5787261676138342e6d6f73737772656e2e766970) |
| 2 | `babak-khoramdin.ir.aysghfkzcxg.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=babak-khoramdin.ir.aysghfkzcxg.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `shsh.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shsh.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `vasalshim.mamadgoli.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vasalshim.mamadgoli.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `se.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `good.cipservice.co.uk` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=good.cipservice.co.uk&port=2083&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `ir.speed.finecooking.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.speed.finecooking.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 8 | `kasu85.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kasu85.tidelark.cc&port=443&secret=eeb8e5365580b9ad3c2ee355dfcbc245e56b61737538352e746964656c61726b2e6363) |
| 9 | `api.godserver52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.godserver52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 10 | `qadim.zhigool.co.uk` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=qadim.zhigool.co.uk&port=22&secret=EERighJJvXrFGRMCIMJdCQ) |
| 11 | `f123.e7.yayayajd.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=f123.e7.yayayajd.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `178.105.107.158` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.107.158&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 13 | `91.107.160.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.160.196&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 14 | `edge.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=edge.proxynet.tech&port=443&secret=ee6ab3febbd991da36e6698e47a1c21687656467652e70726f78796e65742e74656368) |
| 15 | `server2.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server2.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 16 | `aparat.com.filimo.com.namava.ir.telewebion.com.ghoostbusters.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aparat.com.filimo.com.namava.ir.telewebion.com.ghoostbusters.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `panel.hook--tehran.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panel.hook--tehran.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 18 | `95.217.193.223` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.193.223&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 19 | `darya.saheledarya.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=darya.saheledarya.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `dokhtar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dokhtar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
