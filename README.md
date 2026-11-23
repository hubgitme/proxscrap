# 📊 نتایج استخراج: (آخرین بروزرسانی: 02:52 03-09-1405)



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
| 1 | `aparat.com.filimo.com.namava.ir.telewebion.com.ghoostbusters.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aparat.com.filimo.com.namava.ir.telewebion.com.ghoostbusters.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `lllllk.iraj.trsr57d.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lllllk.iraj.trsr57d.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `nocloudnew.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nocloudnew.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `91.221.191.138` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.221.191.138&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `Pn.do.6x.sl.t.9b.80-55-83-16.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Pn.do.6x.sl.t.9b.80-55-83-16.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `3621.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3621.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `my.home.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=my.home.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `41.hide.7y76y.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=41.hide.7y76y.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `freeconnect.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=freeconnect.lol&port=443&secret=eeec15a78c3842e866c302c8526175a68c7975672d6c696e6b2e7275) |
| 10 | `team.fast--pro.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=team.fast--pro.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 11 | `premium.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `cdn1.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn1.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `isaco.ir.jnxu.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=isaco.ir.jnxu.ir&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `star.telbet.lol` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=star.telbet.lol&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `gov.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gov.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 16 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `proxy.foriran.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.foriran.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 18 | `deny72.ashwren.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=deny72.ashwren.xyz&port=443&secret=eea642c4bcbaceb5aa415464da57a03a37706574726f766963682e7275) |
| 19 | `irogallery.golgoli1.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irogallery.golgoli1.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `age.nine11.art` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=age.nine11.art&port=443&secret=2a881c60852b7dd618a1910d57861ff6) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
