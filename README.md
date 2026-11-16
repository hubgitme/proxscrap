# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:07 25-08-1405)



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
| 1 | `78.47.131.66` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=78.47.131.66&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `breezeridge.heronglade.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=breezeridge.heronglade.space&port=8443&secret=eecb583feec28443b065f8a1f3df502eea706574726f766963682e7275) |
| 3 | `darya.saheledarya.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=darya.saheledarya.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `5ti.do.ru7.lq.v.8v.ir.ir.ir.pd.8kmc.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5ti.do.ru7.lq.v.8v.ir.ir.ir.pd.8kmc.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQAAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 5 | `ir.philgent.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.philgent.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 6 | `ir-ir.gnutella2.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.gnutella2.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 7 | `91.98.219.255` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.219.255&port=8443&secret=dd5f7ce28a2c4816c6c923dfd4d5630e01dd) |
| 8 | `name.namenewok.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.namenewok.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `rad.irani-pr.net` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rad.irani-pr.net&port=85&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `checkout.steampower.online` | `3864` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=checkout.steampower.online&port=3864&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `s47n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s47n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `ving.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ving.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `188.245.207.66` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.245.207.66&port=9443&secret=YyEEgYdJXfrFmgMCIMJdjjRueWVrdGFuZXQA) |
| 15 | `khobi-alhamdolelah.ebimarh.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=khobi-alhamdolelah.ebimarh.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 16 | `nigan.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nigan.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `you.nasakhamia.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=you.nasakhamia.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `ccc.horizon555.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ccc.horizon555.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `Hel-hi.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Hel-hi.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 20 | `fame.saalaad.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fame.saalaad.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
