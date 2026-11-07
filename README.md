# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:07 16-08-1405)



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
| 1 | `rond-hamrahaval.ebimarh.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rond-hamrahaval.ebimarh.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 2 | `www.reallygood.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.reallygood.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 3 | `www.manazinjamiram.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.manazinjamiram.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 4 | `dezo23.foxglade.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dezo23.foxglade.xyz&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e64657a6f32332e666f78676c6164652e78797a) |
| 5 | `xxmatrixx.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=xxmatrixx.top&port=853&secret=eee4508d288bf81791177a2f5e73ac06cf6d617472697878782e746f70) |
| 6 | `zenon.flashspder.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zenon.flashspder.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 7 | `ardebill.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ardebill.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 8 | `FOR-IRAN.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=FOR-IRAN.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `IRAN.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=IRAN.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `91.98.107.89` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.107.89&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `91.107.140.144` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.140.144&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 12 | `Help.helps.help` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Help.helps.help&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `178.105.137.152` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.137.152&port=443&secret=eeabf13064a3bf0851a02ad67114f842ce676f6f676c65617069732e636f6d) |
| 14 | `ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 15 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `www.www78-62-184-9.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.www78-62-184-9.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 17 | `luxuryman.sbs` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=luxuryman.sbs&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `169.58.86.18` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=169.58.86.18&port=443&secret=ee85dc3d6c2900e59b6f97f68ee7d1e349676f6f676c65617069732e636f6d) |
| 19 | `support.infinityhalo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=support.infinityhalo.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `mio.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mio.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
