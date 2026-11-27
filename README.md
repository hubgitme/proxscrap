# 📊 نتایج استخراج: (آخرین بروزرسانی: 09:01 06-09-1405)



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
| 1 | `masachoset.rah-toro-mikhanad.info` | `9988` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=masachoset.rah-toro-mikhanad.info&port=9988&secret=e8742282124f08d358551341ead76402) |
| 2 | `5.222.4.90` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.4.90&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `79.137.196.223` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=8443&secret=eeeeacd334a255675ccc880cb6b8c9caf07777772e636c6f7564666c6172652e636f6d) |
| 4 | `85.133.200.11` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.11&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 5 | `amb.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=amb.telehelp.top&port=443&secret=ee5447efddb6d2d618e850c2f2eef65b5964726976652e676f6f676c652e636f6d) |
| 6 | `violet.ashwren.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=violet.ashwren.xyz&port=443&secret=ee6fcf868535df2309ee2f6ea5a6563ef962726f777365722e79616e6465782e7275) |
| 7 | `ir-immortals.sponsorafuture.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-immortals.sponsorafuture.co.uk&port=443&secret=104462821249bd7ac519130220c8dd09) |
| 8 | `hadi-choopan.persian.wolf.ir.aojsnqzcdsc.info` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hadi-choopan.persian.wolf.ir.aojsnqzcdsc.info&port=88&secret=ee0000f00f0f775555fffffff5006e2e69626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `87.248.144.154` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.154&port=8880&secret=3XnjRIGHSb16xRkTAiDCXQk) |
| 10 | `haf.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haf.torob.ir.solzairanbad.ir&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 11 | `winter.lavazem2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=winter.lavazem2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `94.184.39.150` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.184.39.150&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 13 | `worldmaster.varomax.co.uk` | `5500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=worldmaster.varomax.co.uk&port=5500&secret=79e462833349bd7ac519130220c25d10) |
| 14 | `tech.gooodrat.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tech.gooodrat.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 15 | `ohox.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ohox.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `gram.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gram.prxtg.top&port=443&secret=eeabde1be2accd3413ec8e8a0fa256287f64726976652e676f6f676c652e636f6d) |
| 17 | `tassian.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tassian.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `server93.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server93.server-space52.info&port=2020&secret=00000000000000000000000000000000) |
| 19 | `ir-ir.ourmainlands.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.ourmainlands.co.uk&port=443&secret=104462821249bd7ac519130220c8dd09) |
| 20 | `91.234.147.37` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.234.147.37&port=2020&secret=00000000000000000000000000000000) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
