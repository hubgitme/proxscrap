# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:34 06-08-1405)



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
| 1 | `loneny11.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loneny11.tidelark.cc&port=443&secret=ee9267d78681726d5ff1bf826b750ba4ba6c6f6e656e7931312e746964656c61726b2e6363) |
| 2 | `qazmel.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=qazmel.ir&port=443&secret=ee79e344818749bd7ac519130220c25d09706574726f732d65732e636f2e756b) |
| 3 | `api.mangoseason5.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.mangoseason5.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `dashi.estabonita.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dashi.estabonita.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 5 | `rf.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rf.mishutkin.click&port=443&secret=ee5a994c9e79b5e3ff7ec78e7d7e77eb0b72662e6d69736875746b696e2e636c69636b) |
| 6 | `redflag.yazaebalsyadelatproxy.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.vip&port=443&secret=ee24c8636b7e946779a023ee708370719b726564666c61672e79617a616562616c73796164656c617470726f78792e766970) |
| 7 | `ving.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ving.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `run.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=run.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `91.107.171.35` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.171.35&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 10 | `mangoseason8.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mangoseason8.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `Rakhsh.ir.igakwvwa.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Rakhsh.ir.igakwvwa.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `haf.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haf.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `kagato24.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kagato24.mosswren.vip&port=443&secret=eecd7b5204a28b47f7cc34c673574336086b616761746f32342e6d6f73737772656e2e766970) |
| 14 | `89.167.29.101` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.167.29.101&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 15 | `supora40.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=supora40.tidelark.cc&port=443&secret=eea02849a55daccdc7f7a05691b7ef7cd17375706f726134302e746964656c61726b2e6363) |
| 16 | `PAyDaR.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=PAyDaR.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `ir-ir.flipme.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.flipme.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 18 | `Tond.strobox.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Tond.strobox.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 19 | `web.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 20 | `from.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=from.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
