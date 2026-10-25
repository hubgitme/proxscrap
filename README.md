# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:52 03-08-1405)



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
| 1 | `connect.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.mishutkin.click&port=443&secret=ee43b48df152c2246a45ec2f88ea52877264726976652e676f6f676c652e636f6d) |
| 2 | `luxuryman.sbs` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=luxuryman.sbs&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `zozo42.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zozo42.tidelark.cc&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd17a6f7a6f34322e746964656c61726b2e6363) |
| 4 | `65.109.248.100` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.248.100&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `web3.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web3.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `neny42.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=neny42.tidelark.cc&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e6e656e7934322e746964656c61726b2e6363) |
| 7 | `s3.saalaad.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.saalaad.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `delvari.ir.aysghfkzcxg.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=delvari.ir.aysghfkzcxg.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `pulse.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pulse.proxynet.tech&port=443&secret=ee7d4b579bf9027fcacc538af5492a9e6670756c73652e70726f78796e65742e74656368) |
| 10 | `ir-ir.ariely.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.ariely.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 11 | `33.mtprotonewrunningproxasia.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=33.mtprotonewrunningproxasia.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `silnet.varfootball.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silnet.varfootball.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `toleka79.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=toleka79.mosswren.vip&port=443&secret=ee6ce7aa9636179a5f67366aaab4702a26746f6c656b6137392e6d6f73737772656e2e766970) |
| 14 | `mangoseason8.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mangoseason8.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `digi.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `rf.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rf.mishutkin.click&port=443&secret=ee5a994c9e79b5e3ff7ec78e7d7e77eb0b72662e6d69736875746b696e2e636c69636b) |
| 17 | `mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `web.mangoseason7.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.mangoseason7.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `Speed-speed.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Speed-speed.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 20 | `sumi71.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sumi71.mosswren.vip&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b73756d6937312e6d6f73737772656e2e766970) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
