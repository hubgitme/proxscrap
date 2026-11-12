# 📊 نتایج استخراج: (آخرین بروزرسانی: 18:06 21-08-1405)



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
| 1 | `109.70.74.205` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=109.70.74.205&port=443&secret=f36505b7ec3508eb0fd3b7d2e7dada67) |
| 2 | `new.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `mashti-khan.ebimarh.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mashti-khan.ebimarh.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 4 | `pomide92.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pomide92.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e706f6d69646539322e6d6f73737772656e2e766970) |
| 5 | `333.mtprotonewrunningproxasia.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=333.mtprotonewrunningproxasia.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `dema91.larchmere.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dema91.larchmere.xyz&port=443&secret=ee58851f6640315bea58279e83ed6ca84c786170692e6f7a6f6e2e7275) |
| 7 | `speed.runserver.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=speed.runserver.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `pnj.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `333.antony-gordon.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=333.antony-gordon.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `new7.mizanmizanesgh.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new7.mizanmizanesgh.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `195.18.10.204` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.18.10.204&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |
| 12 | `tg2.fkwallet.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg2.fkwallet.online&port=443&secret=ee143d5e3b77f7240638906d3c55cdf050706574726f766963682e7275) |
| 13 | `nocloudnew.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nocloudnew.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `Tond.strobox.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Tond.strobox.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 15 | `mahi.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mahi.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 16 | `pofak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pofak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `nice.rozinalpoku.co.uk` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nice.rozinalpoku.co.uk&port=8080&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `premium.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `91.98.96.120` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.96.120&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `tg.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.proxynet.tech&port=443&secret=ee6d98b7c125f854c0ac73c588ec9f225864726976652e676f6f676c652e636f6d) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
