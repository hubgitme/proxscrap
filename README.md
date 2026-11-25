# 📊 نتایج استخراج: (آخرین بروزرسانی: 09:01 04-09-1405)



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
| 1 | `135.181.74.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.74.183&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 2 | `naznazi.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=naznazi.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `off.namenewok.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=off.namenewok.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `pnj.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.torob.ir.solzairanbad.ir&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 5 | `ir-ir.flipme.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.flipme.info&port=8443&secret=104462821249bd7ac519130220c8dd09) |
| 6 | `a4.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a4.anotelinopalk.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 7 | `nice.rozinalpoku.co.uk` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nice.rozinalpoku.co.uk&port=8080&secret=79e344818749bd7ac519130220c25d09) |
| 8 | `65.109.215.167` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.215.167&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `tehran.bingi.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tehran.bingi.co.uk&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 10 | `209.151.144.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=209.151.144.196&port=443&secret=ee37d89185cc2c0d277a5506e5f18325b1636c6f7564666c6172652e636f6d) |
| 11 | `se.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.ionox.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `dah.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dah.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 13 | `org.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=org.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `violetvalley.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=violetvalley.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9476696f6c657476616c6c65792e7061706572746561706f742e636f6d) |
| 15 | `shoes.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shoes.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `haf.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haf.ionox.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `tg.getrocket.me` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.getrocket.me&port=443&secret=eef84b5bf22712eba2c12b8c0582237add74672e676574726f636b65742e6d65) |
| 18 | `172.245.219.148` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.245.219.148&port=443&secret=ee00000000000000000000000000000000636c6f7564666c6172652e636f6d) |
| 19 | `kasco.alhosein.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kasco.alhosein.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `www.checker-domain.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.checker-domain.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
