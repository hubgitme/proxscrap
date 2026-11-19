# 📊 نتایج استخراج: (آخرین بروزرسانی: 05:45 28-08-1405)



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
| 1 | `narooo.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=narooo.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `vasle.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vasle.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `puot.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=puot.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `Hel-hi.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Hel-hi.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 5 | `11.new1.ramkal12.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=11.new1.ramkal12.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `156.229.161.249` | `5201` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=156.229.161.249&port=5201&secret=ee3a51554a1c8542cc36572fd59c2f63f4617a7572652e6d6963726f736f66742e636f6d) |
| 7 | `harbor.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=harbor.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c94686172626f722e76656c76657477696e646f772e6363) |
| 8 | `w.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=w.prxtg.top&port=443&secret=eec15b39b08e586ff58acd45d81178bf1864726976652e676f6f676c652e636f6d) |
| 9 | `0000way.iraj.trsr57d.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=0000way.iraj.trsr57d.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `kavilo33.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kavilo33.sorrelbay.xyz&port=8443&secret=ee71184e2ac505ed5840dd5a00da3318f3786170692e6f7a6f6e2e7275) |
| 11 | `shomal.bingi.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shomal.bingi.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 12 | `atr.golabkashan.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=atr.golabkashan.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 13 | `hamrah.coudflare.ww.qavi-13.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hamrah.coudflare.ww.qavi-13.co.uk&port=8443&secret=7l984oosSBbGySPf1NVjDgE=) |
| 14 | `tg.getrocket.me` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.getrocket.me&port=443&secret=eef84b5bf22712eba2c12b8c0582237add74672e676574726f636b65742e6d65) |
| 15 | `server63.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server63.server-space52.info&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 16 | `you.nasakhamia.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=you.nasakhamia.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `dokhtar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dokhtar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 18 | `a3.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a3.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `cdn1.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn1.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `Gos.8f.dk.euv.4h.d.kw.68-309-27-46.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Gos.8f.dk.euv.4h.d.kw.68-309-27-46.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
