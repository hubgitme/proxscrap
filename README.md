# 📊 نتایج استخراج: (آخرین بروزرسانی: 21:30 07-08-1405)



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
| 1 | `33.antony-gordon.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=33.antony-gordon.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `nypo47.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nypo47.tidelark.cc&port=443&secret=eeb8e5365580b9ad3c2ee355dfcbc245e56e79706f34372e746964656c61726b2e6363) |
| 3 | `irluxcars.site` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irluxcars.site&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `41.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=41.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `do.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=do.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `167.235.255.168` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.235.255.168&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `cloud-sync-mx.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cloud-sync-mx.online&port=443&secret=ee395b5c5d20a594c5656b17f198621c05636c6f75642d73796e632d6d782e6f6e6c696e65) |
| 8 | `redflag.yazaebalsyadelatproxy.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.vip&port=443&secret=ee9267d78681726d5ff1bf826b750ba4ba726564666c61672e79617a616562616c73796164656c617470726f78792e766970) |
| 9 | `great.cipservice.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=great.cipservice.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `storm.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=storm.proxynet.tech&port=443&secret=ee9fae664efb6f4dace69bb357bfec367773746f726d2e70726f78796e65742e74656368) |
| 11 | `tehran.bingi.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tehran.bingi.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 12 | `digi.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `ir-ir.rebol.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.rebol.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 14 | `web.mangoseason7.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.mangoseason7.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `rootssh2.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rootssh2.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `Dho.phd.iv.md.h.g.if.7.www1www.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Dho.phd.iv.md.h.g.if.7.www1www.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `baran.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=baran.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `94.130.15.206` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.130.15.206&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 19 | `porsorate.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=porsorate.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `api.mangoseason5.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.mangoseason5.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
