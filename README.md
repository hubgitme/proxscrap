# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:53 02-09-1405)



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
| 1 | `www.setado.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.setado.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 2 | `ir-ir.grumpyoldmen.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.grumpyoldmen.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `royaclinic.beauty` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=royaclinic.beauty&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `65.109.106.132` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.106.132&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 5 | `7b.hp.d.f8b.so.y.coe.alo-alo.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7b.hp.d.f8b.so.y.coe.alo-alo.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `AVA.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AVA.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `Ay.pj.fon.7g.kp.v.i8.l.1-2-3-4-5.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ay.pj.fon.7g.kp.v.i8.l.1-2-3-4-5.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `ir.simpleelegance-us.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.simpleelegance-us.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 9 | `nocloudnew.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nocloudnew.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `vizhzhzhzhzh.bypased.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vizhzhzhzhzh.bypased.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 11 | `dizgrakh.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dizgrakh.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `185.19.33.86` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.19.33.86&port=443&secret=eef08dee29bc748ad2f349c593e042bad87777772e6d6963726f736f66742e636f6d) |
| 13 | `91.210.108.83` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.210.108.83&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `206.71.149.70` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=206.71.149.70&port=8080&secret=vshsJGsgKdnhsKenbsYrbbxhdYsbdb2LanndgsfdhAAAAeee) |
| 15 | `irl.firemedia.digital` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irl.firemedia.digital&port=443&secret=eeadd144b0531c1a9f5947e3cb29dc4fd569726c2e666972656d656469612e6469676974616c) |
| 16 | `jadid.zhigool.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadid.zhigool.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `kvas.kemerovo.online` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kvas.kemerovo.online&port=8443&secret=ee888877776666555544443333222211117474322e6d79726b612e6469676974616c) |
| 18 | `you.pelastic.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=you.pelastic.co.uk&port=443&secret=ddc3b375786a3b9630e44cf87d2033a441) |
| 19 | `www.jodaeimanam.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.jodaeimanam.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 20 | `3621.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3621.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
