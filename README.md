# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:24 18-08-1405)



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
| 1 | `rad.irani-pr.net` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rad.irani-pr.net&port=85&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `warp.webproxy.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=warp.webproxy.lol&port=443&secret=eecdd352e63c109299dc978b4e94fc4897776172702e77656270726f78792e6c6f6c) |
| 3 | `chdhk8.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chdhk8.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `Pge.ldi.7g.mk.fs.i.s8.h.kg.37-94-704-33.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Pge.ldi.7g.mk.fs.i.s8.h.kg.37-94-704-33.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `m.lumenpost.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=m.lumenpost.top&port=443&secret=eeadb7cfebd78712e71db745c9da7281b16d2e6c756d656e706f73742e746f70) |
| 6 | `www.setado.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.setado.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 7 | `fast.webproxy.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.webproxy.lol&port=443&secret=ee4160cbb0629c129ad2209f4df88d4bc964726976652e676f6f676c652e636f6d) |
| 8 | `Bur.9h.xju.e.yo.4d.1kp.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Bur.9h.xju.e.yo.4d.1kp.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `Best.IRAN.ir.awedsj.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Best.IRAN.ir.awedsj.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `ir-ir.goaphrodite.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.goaphrodite.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 11 | `77hhjnh79.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77hhjnh79.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `for-ir.speedtestcdn.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=for-ir.speedtestcdn.info&port=8443&secret=dd71889eb517157210d61df330a5f11d95) |
| 13 | `ir-ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 14 | `ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 15 | `5go.hs.ydw.pf4.sgj.fi.t.reallygood.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5go.hs.ydw.pf4.sgj.fi.t.reallygood.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `lora56.tidelark.cc` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lora56.tidelark.cc&port=8443&secret=ee899032aa75159cc1d735f15e7a0e3a6e706574726f766963682e7275) |
| 17 | `we.antony-gordon.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=we.antony-gordon.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `dark-rush-85krcymd.expresshost.cloud` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dark-rush-85krcymd.expresshost.cloud&port=443&secret=eeebd9fc04e4292071437b21c5fcb3e1556461726b2d727573682d38356b7263796d642e65787072657373686f73742e636c6f7564) |
| 19 | `n7d626c.lumenpost.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=n7d626c.lumenpost.top&port=443&secret=ee0b03536395a48484bf73aadee0e37dd46d2e6c756d656e706f73742e746f70) |
| 20 | `Gue.id.6b.2l.du.x8.fi.l.www78-62-184-9.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Gue.id.6b.2l.du.x8.fi.l.www78-62-184-9.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
