# 📊 نتایج استخراج: (آخرین بروزرسانی: 21:02 04-09-1405)



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
  - webproxy, iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn, asr_proxy, proxyskyy, MFDL000

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
| 1 | `do.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=do.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 2 | `this-is.fastnet-vpn.xyz` | `4443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=this-is.fastnet-vpn.xyz&port=4443&secret=ee466f3ef394f7c682a47b604deda898ea746869732d69732e666173746e65742d76706e2e78797a) |
| 3 | `hdoox.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hdoox.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `ram7.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ram7.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `pnj.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 6 | `83.243.86.210` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=83.243.86.210&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `3etare.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3etare.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 8 | `ccc.horizon555.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ccc.horizon555.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `telegram.telbet.app` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=telegram.telbet.app&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 10 | `toka23.kelpmoor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=toka23.kelpmoor.xyz&port=8443&secret=ee8a22a2efc31d03cfe33e7dc2abb809db706574726f766963682e7275) |
| 11 | `shopify.appnormoor.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shopify.appnormoor.info&port=443&secret=dd27729feca8dbcd8008c3fa4f12d92793) |
| 12 | `russia.knox-proxy.world` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=russia.knox-proxy.world&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `gishniz.shambelile.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gishniz.shambelile.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 14 | `79.137.196.223` | `5443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=5443&secret=eeee1b84950935ebf99951bc30e394445c9b7777772e636c6f7564666c6172652e636f6d) |
| 15 | `87.248.144.50` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.50&port=2083&secret=79e344818749bd7ac519130220c25d09) |
| 16 | `85.133.200.13` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.13&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `17fh.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=17fh.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `stream.lovely.lat` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=stream.lovely.lat&port=443&secret=eeaadd88aa9facd454936d0c42dc128e7773747265616d2e6c6f76656c792e6c6174) |
| 19 | `kite.heronglade.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kite.heronglade.space&port=443&secret=eef34d88320a4d0b6e8aaf11541681dd7c706574726f766963682e7275) |
| 20 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
