# 📊 نتایج استخراج: (آخرین بروزرسانی: 00:25 06-09-1405)



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
| 1 | `209.151.144.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=209.151.144.196&port=443&secret=ee37d89185cc2c0d277a5506e5f18325b1636c6f7564666c6172652e636f6d) |
| 2 | `violetvalley.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=violetvalley.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9476696f6c657476616c6c65792e7061706572746561706f742e636f6d) |
| 3 | `char.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 4 | `digi.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `31.hide.7y76y.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.hide.7y76y.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `for-iran.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=for-iran.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `web.cocorichmond.site` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.cocorichmond.site&port=8880&secret=e8742282124f08d358551341ead76402) |
| 8 | `tg.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.prxtg.top&port=443&secret=ee2d1bb45f31056d1063563fc6e38e5a1064726976652e676f6f676c652e636f6d) |
| 9 | `o06d9opx.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=o06d9opx.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `87.248.144.157` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.157&port=8880&secret=dd1603010200010001fc030386e24c3add) |
| 11 | `refiq.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=refiq.poolaki.co.uk&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 12 | `188.40.68.147` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.40.68.147&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 13 | `135.181.74.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.74.183&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 14 | `best.ir.agrescjarkahdgs.info` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=best.ir.agrescjarkahdgs.info&port=88&secret=ee0000f00f0f775555fffffff5006e2e6961626364656667682e696a) |
| 15 | `yek.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yek.torob.ir.solzairanbad.ir&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 16 | `marble.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=marble.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946d6172626c652e7061706572746561706f742e636f6d) |
| 17 | `ir-countdown.lewisj.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-countdown.lewisj.co.uk&port=8443&secret=104462821249bd7ac519130220c8dd09) |
| 18 | `85.133.200.13` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.13&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `3etare.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3etare.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 20 | `derile40.mossharbor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=derile40.mossharbor.xyz&port=8443&secret=ee34fc0a2b54d93b1e88de37d5a16a6d31706574726f766963682e7275) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
