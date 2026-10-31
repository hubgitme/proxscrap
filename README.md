# 📊 نتایج استخراج: (آخرین بروزرسانی: 03:52 09-08-1405)



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
| 1 | `petros-es.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=petros-es.co.uk&port=443&secret=ee79e344818749bd7ac519130220c25d09706574726f732d65732e636f2e756b) |
| 2 | `ir.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `nyne45.foxglade.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nyne45.foxglade.xyz&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e6e796e6534352e666f78676c6164652e78797a) |
| 4 | `ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 5 | `new7.mizanmizanesgh.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new7.mizanmizanesgh.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `volt.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=volt.proxynet.tech&port=443&secret=eecb298408db6b6e0f253d16f508558387766f6c742e70726f78796e65742e74656368) |
| 7 | `Ariobarzanes.ir.igakwvwa.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ariobarzanes.ir.igakwvwa.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `Hel-hi.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Hel-hi.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 9 | `behtarin.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=behtarin.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 11 | `core.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=core.proxynet.tech&port=443&secret=ee6963f54d30b8aa1edf4777718f519652636f72652e70726f78796e65742e74656368) |
| 12 | `vahshianeh.ghodratitarin.info` | `7799` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vahshianeh.ghodratitarin.info&port=7799&secret=dd10400103324995b07c030386e886e7f1) |
| 13 | `www.www1www.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.www1www.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 14 | `razori60.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=razori60.mosswren.vip&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd172617a6f726936302e6d6f73737772656e2e766970) |
| 15 | `www.gasolino.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.gasolino.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 16 | `dokhtar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dokhtar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `zoom.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zoom.proxynet.tech&port=443&secret=eea0ef3f80a42c07d57d95b0ddc070ba017a6f6f6d2e70726f78796e65742e74656368) |
| 18 | `pozo12.saltfern.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pozo12.saltfern.xyz&port=443&secret=ee14697011e0c73f03e95d7b6919a2252b706f7a6f31322e73616c746665726e2e78797a) |
| 19 | `fruit.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fruit.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `old.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=old.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
