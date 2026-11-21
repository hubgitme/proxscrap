# 📊 نتایج استخراج: (آخرین بروزرسانی: 05:28 30-08-1405)



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
| 1 | `www.jodaeimanam.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.jodaeimanam.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 2 | `play.goole.com.craj.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=play.goole.com.craj.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 3 | `95.217.193.223` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.193.223&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 4 | `snapp.ir.neshan.org.tapsi.ir.balad.ir.siyahsefidi.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=snapp.ir.neshan.org.tapsi.ir.balad.ir.siyahsefidi.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `188.206-197-43.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.206-197-43.ir&port=8443&secret=3RBEBIGHSV36xZoDAiDCXLM) |
| 6 | `ir.mediaad.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir.mediaad.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `bookmook.hichibehichi-co.info` | `2882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bookmook.hichibehichi-co.info&port=2882&secret=dd10400103324995b07c030386e886e7f1) |
| 8 | `ardebill.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ardebill.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 9 | `156.229.167.250` | `5201` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=156.229.167.250&port=5201&secret=ee3a51554a1c8542cc36572fd59c2f63f4617a7572652e6d6963726f736f66742e636f6d) |
| 10 | `46.225.35.245` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.35.245&port=443&secret=YyEEgYdJXfrFmgMCIMJdjjRueWVrdGFuZXQA) |
| 11 | `team.fast--pro.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=team.fast--pro.co.uk&port=443&secret=3RBEYoISSb16xRkTAiDCXQk=) |
| 12 | `Rudmoain.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Rudmoain.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 13 | `pnj.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pnj.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `vase-hamas.ir.kjhsdjhads.info` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vase-hamas.ir.kjhsdjhads.info&port=7443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `borujerd-tehran-esfahan.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=borujerd-tehran-esfahan.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 16 | `He.le.y9.bst.xo.t.72-403-837-543.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=He.le.y9.bst.xo.t.72-403-837-543.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 17 | `65.109.98.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.98.231&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 18 | `dh1.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dh1.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `fruit.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fruit.golgoli2.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `soheil.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soheil.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
