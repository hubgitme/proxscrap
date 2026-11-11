# 📊 نتایج استخراج: (آخرین بروزرسانی: 08:10 20-08-1405)



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
| 1 | `vasalshim.mamadgoli.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vasalshim.mamadgoli.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `167.235.255.168` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.235.255.168&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `pishi.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pishi.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 4 | `ir-ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 5 | `server1.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server1.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 6 | `old.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=old.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `silver.ciaude.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silver.ciaude.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `5go.hs.ydw.pf4.sgj.fi.t.reallygood.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5go.hs.ydw.pf4.sgj.fi.t.reallygood.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `char.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `ABOUT.Roo3beh.blog` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ABOUT.Roo3beh.blog&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `warp.webproxy.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=warp.webproxy.lol&port=443&secret=eecdd352e63c109299dc978b4e94fc4897776172702e77656270726f78792e6c6f6c) |
| 12 | `fruit.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fruit.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `no-filter.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=no-filter.ir&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 14 | `Gos.8f.dk.euv.4h.d.kw.68-309-27-46.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Gos.8f.dk.euv.4h.d.kw.68-309-27-46.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `habib-lisanser.browncolor.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=habib-lisanser.browncolor.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 16 | `ir.barhousefarm.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.barhousefarm.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 17 | `refiq.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=refiq.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 18 | `t3.myrka.digital` | `444` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=t3.myrka.digital&port=444&secret=ee8888777766665555444433332222111174332e6d79726b612e6469676974616c) |
| 19 | `Kw.of.pxu.6d.j.210-73-44-9.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Kw.of.pxu.6d.j.210-73-44-9.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `77yjhhk8.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77yjhhk8.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
