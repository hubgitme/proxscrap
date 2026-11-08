# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:14 17-08-1405)



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
| 1 | `5ti.do.ru7.lq.v.8v.ir.ir.ir.pd.8kmc.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5ti.do.ru7.lq.v.8v.ir.ir.ir.pd.8kmc.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQAAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 2 | `ir-ir.panhandleflyers.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.panhandleflyers.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `max.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=max.mishutkin.click&port=443&secret=ee94989d74ad055391384d92c3c773c8d264726976652e676f6f676c652e636f6d) |
| 4 | `pesar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pesar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 5 | `Xog.ofw.5df.og.do.f8.e.w-w-w-w.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Xog.ofw.5df.og.do.f8.e.w-w-w-w.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `91.107.140.144` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.140.144&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 7 | `best-speed.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=best-speed.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `ir-ir.goaphrodite.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.goaphrodite.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 9 | `n7d626c.lumenpost.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=n7d626c.lumenpost.top&port=443&secret=ee0b03536395a48484bf73aadee0e37dd46d2e6c756d656e706f73742e746f70) |
| 10 | `Cu.mp.6h.sp.4d.mip.ts5.f2h.gk.w.13-905-33-84.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Cu.mp.6h.sp.4d.mip.ts5.f2h.gk.w.13-905-33-84.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `fruit.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fruit.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `chd77k7.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chd77k7.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 13 | `persian.gulf.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=persian.gulf.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `mashti-khan.ebimarh.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mashti-khan.ebimarh.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 15 | `Tfi.vp.4f.du.k.t6.di.d.hosinjon.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Tfi.vp.4f.du.k.t6.di.d.hosinjon.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `telegram.telbet.app` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=telegram.telbet.app&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `darya.saheledarya.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=darya.saheledarya.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `7dyyjhhk8.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7dyyjhhk8.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `194.120.230.37` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.37&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 20 | `becarefull.bypased.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=becarefull.bypased.info&port=8443&secret=1603010200010001fc030386e24c3add) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
