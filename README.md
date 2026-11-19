# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:27 28-08-1405)



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
| 1 | `e3fand.fesgheli.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=e3fand.fesgheli.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `sefid.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sefid.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `pomi46.kelpmoor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pomi46.kelpmoor.xyz&port=8443&secret=eef17c22a56cac8bd46d12b91f8f9e102f62726f777365722e79616e6465782e7275) |
| 5 | `sn.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sn.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `5.75.252.233` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.75.252.233&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `isaco.ir.setado.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=isaco.ir.setado.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `91.98.107.89` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.107.89&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `gade59.kelpmoor.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gade59.kelpmoor.xyz&port=443&secret=eef17c22a56cac8bd46d12b91f8f9e102f6f7a6f6e2e7275) |
| 10 | `ir.brettanderson.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.brettanderson.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 11 | `rizolo89.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rizolo89.sorrelbay.xyz&port=8443&secret=ee71184e2ac505ed5840dd5a00da3318f3617669746f2e7275) |
| 12 | `ir.closcloud.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.closcloud.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `Suodbo.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Suodbo.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 14 | `sudoaptupdate-y-sudoaptupgrade-y.logmanfi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sudoaptupdate-y-sudoaptupgrade-y.logmanfi.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 15 | `white.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=white.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `ir.konstruktion.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.konstruktion.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 17 | `digitalvpn-proxy.ru` | `6677` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digitalvpn-proxy.ru&port=6677&secret=73c03865b903152df8e00f8a519ca4a7) |
| 18 | `hamishe.hastim.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hamishe.hastim.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 19 | `5.9.166.250` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.9.166.250&port=8443&secret=1603010200010001fc030386e24c3add) |
| 20 | `tg.boursbato.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.boursbato.ir&port=443&secret=ee47eed690e8a57000cd1c1a1655cc591974672e626f7572736261746f2e6972) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
