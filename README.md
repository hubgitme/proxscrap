# 📊 نتایج استخراج: (آخرین بروزرسانی: 20:17 04-09-1405)



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
| 1 | `run.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=run.golgoli2.co.uk&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 2 | `karbon.torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=karbon.torobchesho.co.uk&port=443&secret=ee79e344828749bd7ac519130220c25d096b6172626f6e2e746f726f6263686573686f2e636f2e756b) |
| 3 | `derile40.mossharbor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=derile40.mossharbor.xyz&port=8443&secret=ee34fc0a2b54d93b1e88de37d5a16a6d31706574726f766963682e7275) |
| 4 | `soh5.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soh5.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `violet.heronglade.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=violet.heronglade.space&port=8443&secret=ee4b20619b99880640b45f275c18e20555786170692e6f7a6f6e2e7275) |
| 6 | `loga86.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loga86.sorrelbay.xyz&port=8443&secret=eee38448c7e07ec8d42dfb2ca4d668b790617669746f2e7275) |
| 7 | `91.107.152.115` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.152.115&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `day.lavazem4.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=day.lavazem4.co.uk&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 9 | `haf.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haf.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 10 | `h2o.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=h2o.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 11 | `galaxy.heronglade.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=galaxy.heronglade.space&port=443&secret=eedac1697485fe37f9c1435848f8ec2ff5786170692e6f7a6f6e2e7275) |
| 12 | `shoes.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shoes.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `org.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=org.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `hasht.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hasht.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 15 | `rimira82.ashwren.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rimira82.ashwren.xyz&port=443&secret=eed9f17e3daed2eba291d36ea30d9aded862726f777365722e79616e6465782e7275) |
| 16 | `edge.turboass.live` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=edge.turboass.live&port=443&secret=ee51116f4018a2b3dfc9bda286c52afe9f656467652e747572626f6173732e6c697665) |
| 17 | `digi.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.golgoli2.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 18 | `1.hide.7y76y.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=1.hide.7y76y.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `harborwinter.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=harborwinter.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c94686172626f7277696e7465722e7061706572746561706f742e636f6d) |
| 20 | `speed-speed.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=speed-speed.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
