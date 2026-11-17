# 📊 نتایج استخراج: (آخرین بروزرسانی: 21:38 26-08-1405)



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
| 1 | `49.12.20.45` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.12.20.45&port=443&secret=7l984oosSBbGySPf1NVjDgE=) |
| 2 | `ir.closcloud.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.closcloud.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `max.fastprx.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=max.fastprx.top&port=443&secret=eecfa453767a4b15622b61914eced5705164726976652e676f6f676c652e636f6d) |
| 4 | `ahvaz.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ahvaz.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `He.le.y9.bst.xo.t.72-403-837-543.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=He.le.y9.bst.xo.t.72-403-837-543.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `checkout.steampower.online` | `3864` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=checkout.steampower.online&port=3864&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `toga43.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=toga43.sorrelbay.xyz&port=8443&secret=eef17c22a56cac8bd46d12b91f8f9e102f62726f777365722e79616e6465782e7275) |
| 8 | `elrmam.bypased.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=elrmam.bypased.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 9 | `ir.genesbyjohn.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.genesbyjohn.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 10 | `3r.ls.u.xjo.s7.h.88-205-694-406.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3r.ls.u.xjo.s7.h.88-205-694-406.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `11.new1.ramkal12.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=11.new1.ramkal12.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `kvas.kemerovo.online` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kvas.kemerovo.online&port=8443&secret=ee888877776666555544443333222211117474322e6d79726b612e6469676974616c) |
| 13 | `exiscos.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=exiscos.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `88.99.126.37` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.126.37&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `www.jodaeimanam.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.jodaeimanam.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 16 | `silver.ciaude.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silver.ciaude.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `ir.peachsoft.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.peachsoft.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 18 | `mile20.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mile20.sorrelbay.xyz&port=8443&secret=eee1d528d13649f8288c1ea7898787b486786170692e6f7a6f6e2e7275) |
| 19 | `tassian.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tassian.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `6h.pe.3.fi.u.fp.66-84-5-947.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6h.pe.3.fi.u.fp.66-84-5-947.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
