# 📊 نتایج استخراج: (آخرین بروزرسانی: 03:01 06-09-1405)



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
| 1 | `87.248.144.249` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.249&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `afkar.lavazem1.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=afkar.lavazem1.co.uk&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 3 | `j7nf.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=j7nf.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 4 | `loga86.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loga86.sorrelbay.xyz&port=8443&secret=eee38448c7e07ec8d42dfb2ca4d668b790617669746f2e7275) |
| 5 | `ir.closcloud.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.closcloud.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `north.tealbriar.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=north.tealbriar.xyz&port=8443&secret=eed8e23b55798e53b64877d42e6ef94a3f706574726f766963682e7275) |
| 7 | `fame.saalaad.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fame.saalaad.info&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 8 | `for.you.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=for.you.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `fable.kelpmoor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fable.kelpmoor.xyz&port=8443&secret=ee6fcf868535df2309ee2f6ea5a6563ef9706574726f766963682e7275) |
| 10 | `61.new1.ramkal12.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=61.new1.ramkal12.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `maman.ir.osahflahyev.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=maman.ir.osahflahyev.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `top.fastprx.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=top.fastprx.top&port=443&secret=ee2eaa3efe26957df17447871a78aa19b064726976652e676f6f676c652e636f6d) |
| 13 | `shsh.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shsh.anotelinopalk.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 14 | `new.nikkhah.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.nikkhah.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 15 | `chat.appnormoor.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chat.appnormoor.info&port=443&secret=dd27729feca8dbcd8008c3fa4f12d92793) |
| 16 | `138.201.223.97` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.201.223.97&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `mile20.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mile20.sorrelbay.xyz&port=8443&secret=eee1d528d13649f8288c1ea7898787b486786170692e6f7a6f6e2e7275) |
| 18 | `plus.khorshid.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=plus.khorshid.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `perfect.lavazem3.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=perfect.lavazem3.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 20 | `152.44.47.172` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=152.44.47.172&port=443&secret=ee3db86f433b3aeb5c115185432b0ca1db636c6f7564666c6172652e636f6d) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
