# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:06 29-07-1405)



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
| 1 | `zovira85.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zovira85.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e7a6f7669726138352e6d6f73737772656e2e766970) |
| 2 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 3 | `do.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=do.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `porsorate.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=porsorate.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `mito38.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mito38.mosswren.vip&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd16d69746f33382e6d6f73737772656e2e766970) |
| 6 | `royaclinic.beauty` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=royaclinic.beauty&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `Speed-speed.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Speed-speed.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 8 | `tig.ofok.tui.frt.7fg7.88n.jananeman.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tig.ofok.tui.frt.7fg7.88n.jananeman.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `mide77.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mide77.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e6d69646537372e6d6f73737772656e2e766970) |
| 10 | `lavashak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lavashak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 11 | `ir.xn--ds-bja.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.xn--ds-bja.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 12 | `7hd78fr.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7hd78fr.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `167.235.255.168` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.235.255.168&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `1.ja.mmd.yayayajd.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=1.ja.mmd.yayayajd.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `dokhtar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dokhtar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 16 | `pofak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pofak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `Fast.finecooking.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fast.finecooking.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 18 | `web-kook.mosbatbashim.info` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web-kook.mosbatbashim.info&port=5500&secret=DDBighLLvXrFGRMCBVJdFQ) |
| 19 | `tazenafas.dingi3.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tazenafas.dingi3.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `new.nakoskoskesh.co.uk` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.nakoskoskesh.co.uk&port=8080&secret=EERighJJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
