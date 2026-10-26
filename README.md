# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:44 04-08-1405)



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
| 1 | `ir.grasic.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.grasic.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 2 | `leomessi.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=leomessi.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `behtarin.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=behtarin.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `swift.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=swift.proxynet.tech&port=443&secret=ee8d8e4465753f6956af2b9531d93ddc1873776966742e70726f78796e65742e74656368) |
| 5 | `s47n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s47n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `333.mtprotonewrunningproxasia.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=333.mtprotonewrunningproxasia.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `qadim.zhigool.co.uk` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=qadim.zhigool.co.uk&port=22&secret=EERighJJvXrFGRMCIMJdCQ) |
| 8 | `r3.saalaad.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r3.saalaad.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `max.kimt.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=max.kimt.click&port=443&secret=ee1b153cf06dbd43c6085c359a6702eb936d61782e6b696d742e636c69636b) |
| 10 | `21.hide.newflamingodomain.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=21.hide.newflamingodomain.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `33.mtprotonewrunningproxasia.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=33.mtprotonewrunningproxasia.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `puot.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=puot.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `jadide.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadide.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `exiscos.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=exiscos.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `3etare.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3etare.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `ir-ir.my-pv.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.my-pv.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 18 | `Magic.godserver52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Magic.godserver52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 19 | `web.mangoseason7.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.mangoseason7.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `kanezo67.tidelark.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kanezo67.tidelark.cc&port=443&secret=eeae5ab45be1bccbba85eec21085b2fd206b616e657a6f36372e746964656c61726b2e6363) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
