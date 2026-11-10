# 📊 نتایج استخراج: (آخرین بروزرسانی: 17:49 19-08-1405)



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
| 1 | `snapp.ir.neshan.org.tapsi.ir.balad.ir.siyahsefidi.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=snapp.ir.neshan.org.tapsi.ir.balad.ir.siyahsefidi.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `xvif.0mhku.cst.8bfy5.hif6.9pn.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=xvif.0mhku.cst.8bfy5.hif6.9pn.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `ir-ir.rebol.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.rebol.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 4 | `bo0ji.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bo0ji.co.uk&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 5 | `4.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=4.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `ir-ir.flipme.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.flipme.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 7 | `Cu.mp.6h.sp.4d.mip.ts5.f2h.gk.w.13-905-33-84.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Cu.mp.6h.sp.4d.mip.ts5.f2h.gk.w.13-905-33-84.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `ir.xn--ds-bja.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.xn--ds-bja.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 9 | `white.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=white.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `nor-bala.flashspder.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nor-bala.flashspder.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 12 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `surge.proxylite.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=surge.proxylite.tech&port=443&secret=7qIJcFetgp2gApkkN8oFR-JzdXJnZS5wcm94eWxpdGUudGVjaA) |
| 14 | `intake.intertextual.jolloped.outvote.unworthy.hapka.info` | `45891` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=intake.intertextual.jolloped.outvote.unworthy.hapka.info&port=45891&secret=eeb579104c16669844b161625dbdcb68f8647a656e2e7275) |
| 15 | `shared4.ddproxy.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shared4.ddproxy.xyz&port=443&secret=eedddddddddddddddddddddddddddddddd6d2e6265626f6f2e7275) |
| 16 | `PAyDaR.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=PAyDaR.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `all.foriran.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=all.foriran.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 18 | `hadaf.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hadaf.golgoli2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `Fud.fo.5n.fod.8h.zj.l.shipboard.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fud.fo.5n.fod.8h.zj.l.shipboard.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `narooo.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=narooo.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
