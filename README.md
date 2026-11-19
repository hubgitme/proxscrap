# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:36 28-08-1405)



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
| 1 | `old.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=old.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `ir-ir.panhandleflyers.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.panhandleflyers.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `pesar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pesar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 5 | `ir-ir.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 6 | `server83.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server83.server-space52.info&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 7 | `tassian.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tassian.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `91.98.107.133` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.107.133&port=8443&secret=1603010200010001fc030386e24c3add) |
| 9 | `digikala.com.torob.ir.divar.ir.basalam.com.eyfst.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digikala.com.torob.ir.divar.ir.basalam.com.eyfst.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `www.setado.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.setado.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 11 | `91.98.101.34` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.101.34&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `dl.linux-orggv.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dl.linux-orggv.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 13 | `jadide.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadide.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `tim.pd.mi.v6.mgi.5s.n.p.wu.basketbalo.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tim.pd.mi.v6.mgi.5s.n.p.wu.basketbalo.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `great.cipservice.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=great.cipservice.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `a3.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a3.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `nocloudnew.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nocloudnew.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `snapp.ir.neshan.org.tapsi.ir.balad.ir.siyahsefidi.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=snapp.ir.neshan.org.tapsi.ir.balad.ir.siyahsefidi.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `ir.vanitydomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.vanitydomain.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 20 | `176.65.135.69` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.65.135.69&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
