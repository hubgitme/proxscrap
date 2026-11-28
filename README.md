# 📊 نتایج استخراج: (آخرین بروزرسانی: 09:01 07-09-1405)



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
| 1 | `bos.bos.be.la.b.et.68-309-27-46.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bos.bos.be.la.b.et.68-309-27-46.ir&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 2 | `bimeh.my-moon.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bimeh.my-moon.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `daryapiano.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=daryapiano.ir&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 4 | `pnj.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.torob.ir.solzairanbad.ir&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `shoes.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shoes.golgoli2.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 6 | `j7nf.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=j7nf.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 7 | `opss.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=opss.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `do.goodrat.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=do.goodrat.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `zendebad.damavand.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zendebad.damavand.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 11 | `rocket.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rocket.telehelp.top&port=443&secret=ee891ce9e0f5fc9fb12e2439fa002d173864726976652e676f6f676c652e636f6d) |
| 12 | `5.222.26.187` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.26.187&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `do.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=do.anotelinopalk.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 14 | `ir-landofgods.fourie.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-landofgods.fourie.co.uk&port=8443&secret=104462821249bd7ac519130220c8dd09) |
| 15 | `light.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=light.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946c696768742e7061706572746561706f742e636f6d) |
| 16 | `noh.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noh.torob.ir.solzairanbad.ir&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 17 | `79.137.196.223` | `18443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=18443&secret=eefd7ec32323aa5b4fc5cdd6b7dd28836a7777772e636c6f7564666c6172652e636f6d) |
| 18 | `ipv4.dablecheckz.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ipv4.dablecheckz.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 19 | `jasminespark.kelpmoor.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jasminespark.kelpmoor.xyz&port=443&secret=eea6765d2e85cb4496f4e0fd16b26b94c4706574726f766963682e7275) |
| 20 | `65.21.227.204` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.21.227.204&port=443&secret=dd79e7010200010007f0030386e24c3add) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
