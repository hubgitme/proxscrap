# 📊 نتایج استخراج: (آخرین بروزرسانی: 07:53 17-08-1405)



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
| 1 | `91.98.107.89` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.107.89&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `cymbal.disuse.guano.intuition.untenantable.teleseryeepesodes.com` | `1900` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cymbal.disuse.guano.intuition.untenantable.teleseryeepesodes.com&port=1900&secret=dd904d82beead0946ade961ecf036a9301) |
| 3 | `pooran.ir.awedsj.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pooran.ir.awedsj.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `xvif.0mhku.cst.8bfy5.hif6.9pn.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=xvif.0mhku.cst.8bfy5.hif6.9pn.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `ir.strawberrybarn.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.strawberrybarn.co.uk&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 6 | `khande-bar-lab-mizanam.lolauth.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=khande-bar-lab-mizanam.lolauth.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 7 | `Ulp.tz.9a.xu.cs.ir.jp.ir.ze8.ir.v6.8kmc.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ulp.tz.9a.xu.cs.ir.jp.ir.ze8.ir.v6.8kmc.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQAAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 8 | `new7.mizanmizanesgh.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new7.mizanmizanesgh.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `tazenafas.dingi3.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tazenafas.dingi3.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `web.mangoseason7.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.mangoseason7.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `max.kimt.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=max.kimt.click&port=443&secret=ee1b153cf06dbd43c6085c359a6702eb936d61782e6b696d742e636c69636b) |
| 12 | `185.121.233.172` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.121.233.172&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `white.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=white.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `se.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `web.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 16 | `rond-hamrahaval.ebimarh.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rond-hamrahaval.ebimarh.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 17 | `severjadid.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=severjadid.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `ir-ir.grumpyoldmen.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.grumpyoldmen.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 19 | `server1.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server1.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 20 | `135.181.74.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.74.183&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
