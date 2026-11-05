# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:58 14-08-1405)



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
| 1 | `for.you.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=for.you.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `baran.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=baran.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `ir.panhandleflyers.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.panhandleflyers.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 4 | `jedi-migi.ebimarh.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jedi-migi.ebimarh.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 5 | `surima18.quietfjord.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=surima18.quietfjord.click&port=443&secret=ee920a4026fcc79354d87c30db9280e578737572696d6131382e7175696574666a6f72642e636c69636b) |
| 6 | `kavi63.fernlark.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kavi63.fernlark.xyz&port=443&secret=ee14697011e0c73f03e95d7b6919a2252b6b61766936332e6665726e6c61726b2e78797a) |
| 7 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `bfesedv.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bfesedv.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `mofid.saheledarya.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mofid.saheledarya.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `losuny65.quietfjord.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=losuny65.quietfjord.click&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b6c6f73756e7936352e7175696574666a6f72642e636c69636b) |
| 11 | `proxy.lodkirmm.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.lodkirmm.ru&port=8443&secret=ee16309abd572d284b309ef26bd7a3f68570726f78792e6c6f646b69726d6d2e7275) |
| 12 | `f123.e7.yayayajd.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=f123.e7.yayayajd.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `www.jodaeimanam.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.jodaeimanam.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 14 | `216.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=216.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `new.nakoskoskesh.co.uk` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.nakoskoskesh.co.uk&port=8080&secret=EERighJJvXrFGRMCIMJdCQ) |
| 16 | `new7.mizanmizanesgh.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new7.mizanmizanesgh.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `nepo53.foxglade.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nepo53.foxglade.xyz&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b6e65706f35332e666f78676c6164652e78797a) |
| 18 | `top.webproxy.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=top.webproxy.lol&port=443&secret=eee301447927b538c6c1a17b223fe3666764726976652e676f6f676c652e636f6d) |
| 19 | `best-speed.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=best-speed.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `server2.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server2.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
