# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:06 07-08-1405)



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
| 1 | `nooshabe.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nooshabe.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 2 | `dokhtar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dokhtar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 3 | `Magic.godserver52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Magic.godserver52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 4 | `46.225.148.183` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.148.183&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `Pooriyaye-vali.ir.igakwvwa.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Pooriyaye-vali.ir.igakwvwa.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `server2.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server2.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 7 | `d1.jadroom.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=d1.jadroom.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 8 | `62.238.62.179` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.62.179&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `ru.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ru.mishutkin.click&port=443&secret=eeb3488e94c4736494021f7b01c7ecf6bf72752e6d69736875746b696e2e636c69636b) |
| 10 | `babak-khoramdin.ir.aysghfkzcxg.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=babak-khoramdin.ir.aysghfkzcxg.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `char.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `ir.groundfloorsolutions.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.groundfloorsolutions.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 13 | `31.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `194.120.230.37` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.37&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 15 | `api.mangoseason5.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.mangoseason5.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `AZADI.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AZADI.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `isaco.ir.setado.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=isaco.ir.setado.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `storm.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=storm.proxynet.tech&port=443&secret=ee9fae664efb6f4dace69bb357bfec367773746f726d2e70726f78796e65742e74656368) |
| 19 | `91.107.171.35` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.171.35&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 20 | `Pasargad.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Pasargad.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
