# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:06 29-08-1405)



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
| 1 | `nor-bala.flashspder.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nor-bala.flashspder.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 2 | `s7n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s7n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `api.mangoseason5.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.mangoseason5.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `mobile.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mobile.prxtg.top&port=443&secret=ee8ae40a2aa7554a058f3340b6449e4e666d6f62696c652e70727874672e746f70) |
| 5 | `felan-by.lolauth.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=felan-by.lolauth.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 6 | `pesar.nanaz.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pesar.nanaz.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 7 | `jhndoes.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jhndoes.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `man-mamnon-misham-aziz.logmanfi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=man-mamnon-misham-aziz.logmanfi.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 9 | `se.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `91.98.97.225` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.97.225&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `foxfrost.heronglade.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=foxfrost.heronglade.space&port=8443&secret=eef34d88320a4d0b6e8aaf11541681dd7c786170692e6f7a6f6e2e7275) |
| 12 | `ram7.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ram7.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `pofak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pofak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 14 | `zenith.lanternmoss.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zenith.lanternmoss.top&port=443&secret=ee3af44f54fb6bb24e664d38ffb1a781197a656e6974682e6c616e7465726e6d6f73732e746f70) |
| 15 | `digikala.com.torob.ir.divar.ir.basalam.com.eyfst.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digikala.com.torob.ir.divar.ir.basalam.com.eyfst.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `mt1.hiesen-proxy.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt1.hiesen-proxy.ru&port=443&secret=ee785147b766a76a27abd34ee1a98a8ec0676f6f676c652e636f6d) |
| 17 | `tazenafas.dingi3.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tazenafas.dingi3.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `hamishe.hastim.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hamishe.hastim.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 19 | `isaco.ir.jnxu.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=isaco.ir.jnxu.ir&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `parts.kemerovo.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=parts.kemerovo.online&port=443&secret=ee1111222233334444555566667777888874342e6d79726b612e6469676974616c) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
