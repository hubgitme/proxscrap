# 📊 نتایج استخراج: (آخرین بروزرسانی: 00:42 20-08-1405)



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
| 1 | `Xog.ofw.5df.og.do.f8.e.w-w-w-w.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Xog.ofw.5df.og.do.f8.e.w-w-w-w.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `Png.lgi.cfe.8vr.xj.f8.b.128-273-66.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Png.lgi.cfe.8vr.xj.f8.b.128-273-66.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `AZADI.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AZADI.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `167.233.233.253` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.233.253&port=8080&secret=YyEEgYdJXfrFmgMCIMJdjjRueWVrdGFuZXQA) |
| 5 | `foc.pf.og.mro.7f.j7.spb.f.lwww.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=foc.pf.og.mro.7f.j7.spb.f.lwww.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `Su.do.hs5.pr.u.9j.uwww.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Su.do.hs5.pr.u.9j.uwww.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `pnj.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `ir.barhousefarm.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.barhousefarm.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 10 | `91.98.107.89` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.107.89&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `panel.hook--tehran.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panel.hook--tehran.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 12 | `silnet.varfootball.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silnet.varfootball.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `tg.getrocket.me` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.getrocket.me&port=443&secret=eef84b5bf22712eba2c12b8c0582237add74672e676574726f636b65742e6d65) |
| 14 | `Pooriyaye-vali.ir.igakwvwa.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Pooriyaye-vali.ir.igakwvwa.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `tassian.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tassian.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `proxy.foriran.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.foriran.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `185.166.214.158` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.166.214.158&port=8443&secret=7n3yZ_5IshU33VFu-RJW7fZ3d3cuYXBwbGUuY29t) |
| 18 | `s47n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s47n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `Speed-speed.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Speed-speed.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 20 | `45.195.250.70` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.195.250.70&port=443&secret=ddb83572a117470fd34eee07134d361f0b) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
