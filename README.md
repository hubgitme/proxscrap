# 📊 نتایج استخراج: (آخرین بروزرسانی: 00:53 12-08-1405)



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
| 1 | `dashi.estabonita.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dashi.estabonita.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 2 | `darya.naaab.lol` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=darya.naaab.lol&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `77.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.mishutkin.click&port=443&secret=eec8017bc0cd6ea4b51ca268fb7b3aba6237372e6d69736875746b696e2e636c69636b) |
| 4 | `ir.dinocol.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.dinocol.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 5 | `noh.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noh.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `zoom.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zoom.proxynet.tech&port=443&secret=eea0ef3f80a42c07d57d95b0ddc070ba017a6f6f6d2e70726f78796e65742e74656368) |
| 7 | `ir-ir.engematica.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.engematica.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 8 | `nema57.quietfjord.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nema57.quietfjord.click&port=443&secret=eeb8e5365580b9ad3c2ee355dfcbc245e56e656d6135372e7175696574666a6f72642e636c69636b) |
| 9 | `sn.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sn.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `188.206-197-43.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.206-197-43.ir&port=8443&secret=3RBEBIGHSV36xZoDAiDCXLM) |
| 11 | `lolo89.larchmere.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lolo89.larchmere.xyz&port=443&secret=ee24c8636b7e946779a023ee708370719b6c6f6c6f38392e6c617263686d6572652e78797a) |
| 12 | `mashti.just-money.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mashti.just-money.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 13 | `behtarin.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=behtarin.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `ir-ir.panhandleflyers.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.panhandleflyers.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 15 | `77.42.115.87` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.42.115.87&port=8080&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `org.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=org.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `kasco.alhosein.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kasco.alhosein.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `sarzamin.mosbatbashim.info` | `2882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sarzamin.mosbatbashim.info&port=2882&secret=dd10400103324995b07c030386e886e7f1) |
| 19 | `62.238.62.179` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.62.179&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `termsnal.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=termsnal.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
