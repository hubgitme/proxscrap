# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:01 18-08-1405)



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
| 1 | `jadide.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadide.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `www.yesyesno.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.yesyesno.ir&port=8443&secret=3RcBGGq9DqYBIxkuJkNPkaU) |
| 3 | `proxy.foriran.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.foriran.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 4 | `jadid.porsorate.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadid.porsorate.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `tonyzo46.birchquay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tonyzo46.birchquay.xyz&port=8443&secret=eeae5ab45be1bccbba85eec21085b2fd20706574726f766963682e7275) |
| 6 | `Ulp.tz.9a.xu.cs.ir.jp.ir.ze8.ir.v6.8kmc.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ulp.tz.9a.xu.cs.ir.jp.ir.ze8.ir.v6.8kmc.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQAAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 7 | `91.98.109.248` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.109.248&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `panel.hook--tehran.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panel.hook--tehran.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 9 | `bfesedv.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bfesedv.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `pesar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pesar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 11 | `78.47.131.47` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=78.47.131.47&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `sefid.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sefid.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `jadid.zhigool.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadid.zhigool.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 14 | `warp.webproxy.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=warp.webproxy.lol&port=443&secret=eecdd352e63c109299dc978b4e94fc4897776172702e77656270726f78792e6c6f6c) |
| 15 | `62.238.63.143` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.63.143&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `strong.hosiyaman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=strong.hosiyaman.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 17 | `im.dumaniltd.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=im.dumaniltd.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `persian.gulf.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=persian.gulf.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 19 | `fast.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.mishutkin.click&port=443&secret=eef767ebee5708dadc985d58ad6e04560664726976652e676f6f676c652e636f6d) |
| 20 | `194.120.230.37` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.37&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
