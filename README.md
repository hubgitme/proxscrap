# 📊 نتایج استخراج: (آخرین بروزرسانی: 00:44 30-07-1405)



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
| 1 | `severjadid.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=severjadid.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `nooshabe.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nooshabe.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 3 | `aseman.lunavane.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aseman.lunavane.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `tex.l1.mu.pe.6c.bep.0y.xd.n.te.77-35-93-6.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tex.l1.mu.pe.6c.bep.0y.xd.n.te.77-35-93-6.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `ir.xn--ds-bja.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.xn--ds-bja.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 6 | `AVA.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AVA.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `qadim.zhigool.co.uk` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=qadim.zhigool.co.uk&port=22&secret=EERighJJvXrFGRMCIMJdCQ) |
| 8 | `95.216.220.240` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.220.240&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `panel.hook--tehran.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panel.hook--tehran.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 10 | `tokane46.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tokane46.tidelark.cc&port=443&secret=eeae5ab45be1bccbba85eec21085b2fd20746f6b616e6534362e746964656c61726b2e6363) |
| 11 | `sarzamin.mosbatbashim.info` | `2882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sarzamin.mosbatbashim.info&port=2882&secret=dd10400103324995b07c030386e886e7f1) |
| 12 | `21.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=21.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `iranmaster29.suser.ir` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iranmaster29.suser.ir&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 14 | `tg.surfvpn.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.surfvpn.info&port=443&secret=eedf44a4347c1eb8938c7e63340bd1ca4972656c61792e7375726676706e2e617070) |
| 15 | `new7.mizanmizanesgh.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new7.mizanmizanesgh.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `mazo84.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mazo84.tidelark.cc&port=443&secret=ee214011ba04108a7b1836df3a5e918b3b6d617a6f38342e746964656c61726b2e6363) |
| 17 | `Cu.mp.6h.sp.4d.mip.ts5.f2h.gk.w.13-905-33-84.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Cu.mp.6h.sp.4d.mip.ts5.f2h.gk.w.13-905-33-84.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `3.assassinationpuma.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.assassinationpuma.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `156.239.251.57` | `17068` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=156.239.251.57&port=17068&secret=ee1547b025141a8925dd41438a0a70377a7777772e6d6963726f736f66742e636f6d) |
| 20 | `33.antifilterasianew.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=33.antifilterasianew.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
