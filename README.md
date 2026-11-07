# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:07 16-08-1405)



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
| 1 | `62.238.63.143` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.63.143&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `ir.dinocol.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.dinocol.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `Ariobarzanes.ir.igakwvwa.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ariobarzanes.ir.igakwvwa.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `estevia.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=estevia.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 5 | `you.nasakhamia.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=you.nasakhamia.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `math-test.bypased.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=math-test.bypased.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 7 | `kranch.golabkashan.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kranch.golabkashan.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 8 | `narooo.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=narooo.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `strong.hosiyaman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=strong.hosiyaman.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 10 | `abo-ali-sina.basalam.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=abo-ali-sina.basalam.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 11 | `web3.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web3.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `dark-rush-85krcymd.expresshost.cloud` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dark-rush-85krcymd.expresshost.cloud&port=443&secret=eeebd9fc04e4292071437b21c5fcb3e1556461726b2d727573682d38356b7263796d642e65787072657373686f73742e636c6f7564) |
| 13 | `bfesedv.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bfesedv.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `164.37.224.216` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=164.37.224.216&port=443&secret=ddc62c6006d0a383e80aab9f1b8a233856) |
| 15 | `proxy.nizya.club` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.nizya.club&port=443&secret=ee05cf8e164f926f4a664b2404d276a1d670726f78792e6e697a79612e636c7562) |
| 16 | `31.57.166.178` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.57.166.178&port=443&secret=eedddddddddddddddddddddddddddddddd6d2e6265626f6f2e7275) |
| 17 | `Pooriyaye-vali.ir.igakwvwa.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Pooriyaye-vali.ir.igakwvwa.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `333.mtprotonewrunningproxasia.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=333.mtprotonewrunningproxasia.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `cdn1.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn1.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `www.13-905-33-84.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.13-905-33-84.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
