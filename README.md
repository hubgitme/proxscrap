# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:44 30-07-1405)



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
| 1 | `refiq.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=refiq.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 2 | `rootssh2.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rootssh2.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `premium.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `33.mtprotonewrunningproxasia.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=33.mtprotonewrunningproxasia.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `ving.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ving.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 7 | `Rudmoain.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Rudmoain.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 8 | `156.239.251.33` | `24860` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=156.239.251.33&port=24860&secret=ee1547b025141a8925dd41438a0a70377a7777772e6d6963726f736f66742e636f6d) |
| 9 | `mimizo19.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mimizo19.tidelark.cc&port=443&secret=ee6ce7aa9636179a5f67366aaab4702a266d696d697a6f31392e746964656c61726b2e6363) |
| 10 | `for.you.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=for.you.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `ir.genesbyjohn.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.genesbyjohn.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 12 | `65.109.248.100` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.248.100&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `park.monik.hamintori.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=park.monik.hamintori.co.uk&port=443&secret=7l984oosSBbGySPf1NVjDgE=) |
| 14 | `www.www1www.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.www1www.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 15 | `pnj.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `raga84.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=raga84.mosswren.vip&port=443&secret=ee920a4026fcc79354d87c30db9280e5787261676138342e6d6f73737772656e2e766970) |
| 17 | `65.109.247.97` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.247.97&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `Suodbo.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Suodbo.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 19 | `panel.hook--tehran.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panel.hook--tehran.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 20 | `ponyny28.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ponyny28.tidelark.cc&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd1706f6e796e7932382e746964656c61726b2e6363) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
