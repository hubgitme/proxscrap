# 📊 نتایج استخراج: (آخرین بروزرسانی: 08:23 23-08-1405)



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
| 1 | `www.torbad.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.torbad.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 2 | `ir.closcloud.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.closcloud.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `ir-ir.gnutella2.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.gnutella2.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 4 | `server93.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server93.server-space52.info&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 5 | `dashi.estabonita.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dashi.estabonita.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 6 | `rad.irani-pr.net` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rad.irani-pr.net&port=85&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `isaco.ir.setado.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=isaco.ir.setado.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `bookmook.hichibehichi-co.info` | `2882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bookmook.hichibehichi-co.info&port=2882&secret=dd10400103324995b07c030386e886e7f1) |
| 9 | `haji-jan.golabkashan.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haji-jan.golabkashan.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 10 | `vimika15.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vimika15.tidelark.cc&port=443&secret=ee4abe44348ba405ac59448f7f9fe6353c706574726f766963682e7275) |
| 11 | `ir-ir.rebol.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.rebol.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 12 | `ir.genesbyjohn.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.genesbyjohn.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 13 | `613.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=613.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `www.jodaeimanam.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.jodaeimanam.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 15 | `aparat.com.filimo.com.namava.ir.telewebion.com.ghoostbusters.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aparat.com.filimo.com.namava.ir.telewebion.com.ghoostbusters.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `21.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=21.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `143.14.59.80` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=143.14.59.80&port=8080&secret=vshsJGsgKdnhsKenbsYrbbxhdYsbdb2LanndgsfdhAAAAeee) |
| 18 | `kasco.alhosein.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kasco.alhosein.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `pintrest-cool.browncolor.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pintrest-cool.browncolor.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 20 | `91.234.147.10` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.234.147.10&port=2020&secret=00000000000000000000000000000000) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
