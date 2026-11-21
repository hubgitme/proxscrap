# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:11 30-08-1405)



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
| 1 | `a5.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a5.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `www.99-99-63-75.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.99-99-63-75.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 3 | `jadid.zhigool.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadid.zhigool.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 4 | `31.57.185.235` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.57.185.235&port=443&secret=dd890938bf53a1dab0a211a217a9260763) |
| 5 | `noon.begir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noon.begir.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 6 | `195.18.10.204` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.18.10.204&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |
| 7 | `Tfi.vp.4f.du.k.t6.di.d.hosinjon.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Tfi.vp.4f.du.k.t6.di.d.hosinjon.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `nexora.logmanfi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nexora.logmanfi.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 9 | `172.65.62.96` | `49955` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.62.96&port=49955&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `solar.heronglade.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=solar.heronglade.space&port=443&secret=ee4b20619b99880640b45f275c18e20555706574726f766963682e7275) |
| 11 | `bo0ji.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bo0ji.co.uk&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 12 | `aseman.lunavane.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aseman.lunavane.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `6h.pe.3.fi.u.fp.66-84-5-947.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6h.pe.3.fi.u.fp.66-84-5-947.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `H2O.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=H2O.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 15 | `Ny.lgu.d.f8.fi.r.93-22-74-38.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ny.lgu.d.f8.fi.r.93-22-74-38.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `baran.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=baran.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `orchid.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=orchid.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946f72636869642e76656c76657477696e646f772e6363) |
| 18 | `Mo.heo.u1.gof.so.5g.k.505-808-404-202.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Mo.heo.u1.gof.so.5g.k.505-808-404-202.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `royaclinic.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=royaclinic.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `FOR-IRAN.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=FOR-IRAN.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
