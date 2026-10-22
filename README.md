# 📊 نتایج استخراج: (آخرین بروزرسانی: 00:41 01-08-1405)



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
| 1 | `milo44.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=milo44.mosswren.vip&port=443&secret=eefd9a9e2ac2851ddc327fe5971e25a87d6d696c6f34342e6d6f73737772656e2e766970) |
| 2 | `zovira85.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zovira85.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e7a6f7669726138352e6d6f73737772656e2e766970) |
| 3 | `7hd78fr.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7hd78fr.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `im.dumaniltd.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=im.dumaniltd.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `topo15.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=topo15.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e746f706f31352e6d6f73737772656e2e766970) |
| 6 | `ir.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `raga84.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=raga84.mosswren.vip&port=443&secret=ee920a4026fcc79354d87c30db9280e5787261676138342e6d6f73737772656e2e766970) |
| 8 | `glo.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=glo.mishutkin.click&port=443&secret=eef214f8fd864040db94f533c47bd76781676c6f2e6d69736875746b696e2e636c69636b) |
| 9 | `33.mtprotonewrunningproxasia.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=33.mtprotonewrunningproxasia.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `ir.flipme.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.flipme.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 11 | `178.104.115.71` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.115.71&port=443&secret=YyEEgYdJXfrFmgMCIMJdjjRueWVrdGFuZXQA) |
| 12 | `tig.ofok.tui.frt.7fg7.88n.jananeman.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tig.ofok.tui.frt.7fg7.88n.jananeman.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `my-iran.vingardium.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=my-iran.vingardium.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 14 | `redflag.yazaebalsyadelatproxy.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.uk&port=443&secret=ee69e899d89ec68e220ca177557322b27f726564666c61672e79617a616562616c73796164656c617470726f78792e6363) |
| 15 | `mito38.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mito38.mosswren.vip&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd16d69746f33382e6d6f73737772656e2e766970) |
| 16 | `toka21.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=toka21.mosswren.vip&port=443&secret=ee9267d78681726d5ff1bf826b750ba4ba746f6b6132312e6d6f73737772656e2e766970) |
| 17 | `hadaf.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hadaf.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `hash.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hash.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `91.98.100.233` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.100.233&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `new.lambforkebeb.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.lambforkebeb.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
