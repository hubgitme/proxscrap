# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:13 22-08-1405)



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
| 1 | `narooo.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=narooo.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `ir.lv223.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.lv223.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 3 | `65.108.209.51` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.108.209.51&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `bookmook.hichibehichi-co.info` | `2882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bookmook.hichibehichi-co.info&port=2882&secret=dd10400103324995b07c030386e886e7f1) |
| 5 | `server83.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server83.server-space52.info&port=2020&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 6 | `6h.pe.3.fi.u.fp.66-84-5-947.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6h.pe.3.fi.u.fp.66-84-5-947.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `ir-ir.my-pv.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.my-pv.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 8 | `ccc.horizon555.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ccc.horizon555.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `zolole21.larchmere.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zolole21.larchmere.xyz&port=8443&secret=eeb0a621aecd97816306c197d21a8bf47b786170692e6f7a6f6e2e7275) |
| 10 | `digikala.com.torob.ir.divar.ir.basalam.com.eyfst.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digikala.com.torob.ir.divar.ir.basalam.com.eyfst.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `vasl-sho-eshgh-kon.ir.bcsadwtgd.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vasl-sho-eshgh-kon.ir.bcsadwtgd.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `78.46.240.254` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=78.46.240.254&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `tg.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.prxtg.top&port=443&secret=ee2d1bb45f31056d1063563fc6e38e5a1064726976652e676f6f676c652e636f6d) |
| 14 | `awd.subaru-volga.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=awd.subaru-volga.com&port=443&secret=ee1111222233334444555566667777888874342e6d79726b612e6469676974616c) |
| 15 | `ir.ataman.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.ataman.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 16 | `isaco.ir.jnxu.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=isaco.ir.jnxu.ir&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `boro.poolaki.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boro.poolaki.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 18 | `link.steampower.online` | `3864` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=link.steampower.online&port=3864&secret=79e344818749bd7ac519130220c25d09) |
| 19 | `white.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=white.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `ir-ir.naganuma.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.naganuma.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
