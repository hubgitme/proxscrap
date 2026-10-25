# 📊 نتایج استخراج: (آخرین بروزرسانی: 02:31 04-08-1405)



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
| 1 | `refiq.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=refiq.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 2 | `159.69.9.248` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=159.69.9.248&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `redflag.yazaebalsyadelatproxy.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.uk&port=443&secret=ee69e899d89ec68e220ca177557322b27f726564666c61672e79617a616562616c73796164656c617470726f78792e6363) |
| 4 | `edge.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=edge.proxynet.tech&port=443&secret=ee6ab3febbd991da36e6698e47a1c21687656467652e70726f78796e65742e74656368) |
| 5 | `narooo.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=narooo.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `redflag.yazaebalsyadelatproxy.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.com&port=443&secret=ee69e899d89ec68e220ca177557322b27f726564666c61672e79617a616562616c73796164656c617470726f78792e6363) |
| 7 | `ir-ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 8 | `delvari.ir.aysghfkzcxg.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=delvari.ir.aysghfkzcxg.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `vasalshim.mamadgoli.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vasalshim.mamadgoli.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `x.shmelproxy.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=x.shmelproxy.top&port=443&secret=eefc2612ff65a557fddf1d1b334395ef237975672d6c696e6b2e7275) |
| 11 | `silnet.varfootball.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=silnet.varfootball.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `Speed-speed.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Speed-speed.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 13 | `dns.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dns.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `ir-ir.gnutella2.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.gnutella2.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 15 | `connect.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.mishutkin.click&port=443&secret=ee43b48df152c2246a45ec2f88ea52877264726976652e676f6f676c652e636f6d) |
| 16 | `fast.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.mishutkin.click&port=443&secret=eef767ebee5708dadc985d58ad6e04560664726976652e676f6f676c652e636f6d) |
| 17 | `web.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 18 | `one.horizon555.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=one.horizon555.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `meshki.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=meshki.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `tg.fiveg.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.fiveg.vip&port=443&secret=7i5IMwtNg7cXYO7ArXm2H7x0Zy5maXZlZy52aXA) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
