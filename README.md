# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:25 19-08-1405)



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
| 1 | `46.224.67.119` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.224.67.119&port=443&secret=YyEEgYdJXfrFmgMCIMJdjjRueWVrdGFuZXQA) |
| 2 | `Ny.lgu.d.f8.fi.r.93-22-74-38.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ny.lgu.d.f8.fi.r.93-22-74-38.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `80.47.237.160` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=80.47.237.160&port=443&secret=ee25b1bc7a41ce6f19d3478a88120545b2646f63732e6461726b6269742e646576) |
| 4 | `khare-gol.golabkashan.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=khare-gol.golabkashan.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 5 | `hadaf.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hadaf.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `ir-ir.naganuma.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.naganuma.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 7 | `silnet.varfootball.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silnet.varfootball.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `white.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=white.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `xenon.foriran.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=xenon.foriran.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 10 | `ir-ir.gnutella2.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.gnutella2.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 11 | `AVA.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AVA.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `7b.hp.d.f8b.so.y.coe.alo-alo.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7b.hp.d.f8b.so.y.coe.alo-alo.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `kranch.golabkashan.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kranch.golabkashan.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 14 | `185.166.214.158` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.166.214.158&port=8443&secret=7n3yZ_5IshU33VFu-RJW7fZ3d3cuYXBwbGUuY29t) |
| 15 | `storagexx.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=storagexx.space&port=443&secret=ee24b61556a3ec49bc0c7a5a7e8525702873746f7261676578782e7370616365) |
| 16 | `Yfo.ogr.8fk.hd3.fi.c.ye.o.gasolino.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Yfo.ogr.8fk.hd3.fi.c.ye.o.gasolino.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `8j.nm.dor.pd.dp.setado.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=8j.nm.dor.pd.dp.setado.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `sarma.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sarma.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 19 | `dh1.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dh1.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `Qin.do.c9.tsj.dl.y4.servervijhe.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Qin.do.c9.tsj.dl.y4.servervijhe.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
