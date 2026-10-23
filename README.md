# 📊 نتایج استخراج: (آخرین بروزرسانی: 03:18 02-08-1405)



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
| 1 | `ultra.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ultra.mishutkin.click&port=443&secret=eed02e349163d9ea4376a2ae6a94fc550b64726976652e676f6f676c652e636f6d) |
| 2 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `dns.speed-benz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dns.speed-benz.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `bastani.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bastani.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 5 | `new7.mizanmizanesgh.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new7.mizanmizanesgh.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `nfc.neo-duo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nfc.neo-duo.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 7 | `138.199.149.10` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.199.149.10&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 8 | `mide77.mosswren.vip` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mide77.mosswren.vip&port=443&secret=ee899032aa75159cc1d735f15e7a0e3a6e6d69646537372e6d6f73737772656e2e766970) |
| 9 | `vasalshim.mamadgoli.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vasalshim.mamadgoli.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `redflag.yazaebalsyadelatproxy.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=redflag.yazaebalsyadelatproxy.co.uk&port=443&secret=ee69e899d89ec68e220ca177557322b27f726564666c61672e79617a616562616c73796164656c617470726f78792e6363) |
| 11 | `Speed-speed.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Speed-speed.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 12 | `tg.getsurfvpn.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.getsurfvpn.com&port=443&secret=eedf44a4347c1eb8938c7e63340bd1ca4972656c61792e7375726676706e2e617070) |
| 13 | `194.120.230.106` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.106&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 14 | `great.cipservice.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=great.cipservice.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `tex.l1.mu.pe.6c.bep.0y.xd.n.te.77-35-93-6.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tex.l1.mu.pe.6c.bep.0y.xd.n.te.77-35-93-6.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `fast.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.proxynet.tech&port=443&secret=ee08787a2b7fd3220d9d35679aab082cab666173742e70726f78796e65742e74656368) |
| 17 | `dizgrakh.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dizgrakh.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `eyiran1.suser.ir` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=eyiran1.suser.ir&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 19 | `www.www1www.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.www1www.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 20 | `bo0ji.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bo0ji.co.uk&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
