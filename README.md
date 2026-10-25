# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:39 03-08-1405)



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
| 1 | `ll6j.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ll6j.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `138.199.149.10` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.199.149.10&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `mazo84.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mazo84.tidelark.cc&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b6d617a6f38342e746964656c61726b2e6363) |
| 4 | `haf.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haf.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `Rudmoain.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Rudmoain.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 6 | `panir.begir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panir.begir.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 7 | `reyhoon.shambelile.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=reyhoon.shambelile.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 8 | `Suodbo.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Suodbo.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 9 | `dns.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dns.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `AZADI.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AZADI.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `delvari.ir.aysghfkzcxg.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=delvari.ir.aysghfkzcxg.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `fast.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.proxynet.tech&port=443&secret=ee08787a2b7fd3220d9d35679aab082cab666173742e70726f78796e65742e74656368) |
| 13 | `redflag.yazaebalsyadelatproxy.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.com&port=443&secret=ee69e899d89ec68e220ca177557322b27f726564666c61672e79617a616562616c73796164656c617470726f78792e6363) |
| 14 | `Ariobarzanes.ir.igakwvwa.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ariobarzanes.ir.igakwvwa.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `kavima49.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kavima49.mosswren.vip&port=443&secret=ee6ce7aa9636179a5f67366aaab4702a266b6176696d6134392e6d6f73737772656e2e766970) |
| 16 | `ir-ir.engematica.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.engematica.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 17 | `maka61.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=maka61.tidelark.cc&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e6d616b6136312e746964656c61726b2e6363) |
| 18 | `raga84.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=raga84.mosswren.vip&port=443&secret=ee920a4026fcc79354d87c30db9280e5787261676138342e6d6f73737772656e2e766970) |
| 19 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `m6m6.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=m6m6.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
