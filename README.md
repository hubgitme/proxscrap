# 📊 نتایج استخراج: (آخرین بروزرسانی: 00:28 10-08-1405)



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
| 1 | `ir-ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdC) |
| 2 | `cdn1.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn1.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `www.www78-62-184-9.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.www78-62-184-9.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 4 | `volt.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=volt.proxynet.tech&port=443&secret=eecb298408db6b6e0f253d16f508558387766f6c742e70726f78796e65742e74656368) |
| 5 | `yarypple.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yarypple.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `178.105.201.7` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.201.7&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 7 | `159.69.9.248` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=159.69.9.248&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `ir.genesbyjohn.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.genesbyjohn.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 9 | `www.13-905-33-84.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.13-905-33-84.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 10 | `giga.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=giga.proxynet.tech&port=443&secret=ee749e956929a5ff74e4fcd4b656b6cb4d676967612e70726f78796e65742e74656368) |
| 11 | `196.19.243.197` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=196.19.243.197&port=443&secret=7j2yWGeEZqfM65fTER6Yy5t3aWxkYmVycmllcy5ydQ) |
| 12 | `ir.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 13 | `jhndoes.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jhndoes.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `93.113.230.145` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=93.113.230.145&port=443&secret=FASTooGmYdaaVxJpA0SkKQ) |
| 15 | `65.109.98.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.98.231&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 16 | `ir.strawberrybarn.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.strawberrybarn.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 17 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 18 | `core.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=core.proxynet.tech&port=443&secret=ee6963f54d30b8aa1edf4777718f519652636f72652e70726f78796e65742e74656368) |
| 19 | `royaclinic.beauty` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=royaclinic.beauty&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `s3.soft98.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.soft98.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
