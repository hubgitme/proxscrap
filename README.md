# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:12 01-09-1405)



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
| 1 | `Ay.pj.fon.7g.kp.v.i8.l.1-2-3-4-5.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ay.pj.fon.7g.kp.v.i8.l.1-2-3-4-5.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `max.fastprx.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=max.fastprx.top&port=443&secret=eecfa453767a4b15622b61914eced5705164726976652e676f6f676c652e636f6d) |
| 3 | `91.221.190.198` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.221.190.198&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `termsnal.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=termsnal.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `www.servertala.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.servertala.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 6 | `FOR-IRAN.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=FOR-IRAN.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `188.206-197-43.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.206-197-43.ir&port=8443&secret=3RBEBIGHSV36xZoDAiDCXLM) |
| 8 | `45.144.137.187` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.144.137.187&port=8443&secret=ee6e04aca4d889da40cb3bb10cb081b8c37777772e6d6963726f736f66742e636f6d) |
| 9 | `gole-sorati.golabkashan.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gole-sorati.golabkashan.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 10 | `236f1.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=236f1.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `light.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=light.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946c696768742e76656c76657477696e646f772e6363) |
| 12 | `61.new1.ramkal12.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=61.new1.ramkal12.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `bookmook.hichibehichi-co.info` | `2882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bookmook.hichibehichi-co.info&port=2882&secret=dd10400103324995b07c030386e886e7f1) |
| 14 | `fame.saalaad.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fame.saalaad.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `w.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=w.prxtg.top&port=443&secret=eec15b39b08e586ff58acd45d81178bf1864726976652e676f6f676c652e636f6d) |
| 16 | `age.nine11.art` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=age.nine11.art&port=443&secret=86dbc3a5c345151b18f2843d8291c683) |
| 17 | `a4.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a4.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `loga86.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loga86.sorrelbay.xyz&port=8443&secret=eee38448c7e07ec8d42dfb2ca4d668b790617669746f2e7275) |
| 19 | `www.setado.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.setado.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 20 | `silver.ciaude.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silver.ciaude.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
