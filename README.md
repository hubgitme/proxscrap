# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:51 13-08-1405)



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
| 1 | `iran.bingi.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iran.bingi.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 2 | `severjadid.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=severjadid.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `web3.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web3.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 4 | `new.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `Suodbo.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Suodbo.co.uk&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 6 | `135.181.74.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.74.189&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 7 | `ahvaz.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ahvaz.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `white.magli200.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=white.magli200.info&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `ir-ir.gnutella2.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.gnutella2.info&port=8443&secret=EERighJJvXrFGRMCIMjdCQ) |
| 10 | `web3.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web3.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `portal.flashspder.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=portal.flashspder.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 12 | `royaclinic.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=royaclinic.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `legato86.quietfjord.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=legato86.quietfjord.click&port=443&secret=eeae5ab45be1bccbba85eec21085b2fd206c656761746f38362e7175696574666a6f72642e636c69636b) |
| 14 | `www.gasolino.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.gasolino.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 15 | `max.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=max.mishutkin.click&port=443&secret=ee94989d74ad055391384d92c3c773c8d264726976652e676f6f676c652e636f6d) |
| 16 | `soh5.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soh5.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `Help.helps.help` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Help.helps.help&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `topproxt.asia` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=topproxt.asia&port=443&secret=eebbb00c5d6d8a742b1a762499eb7d4912617669746f2e7275) |
| 19 | `Fast.finecooking.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fast.finecooking.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 20 | `polo57.quietfjord.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=polo57.quietfjord.click&port=443&secret=ee14697011e0c73f03e95d7b6919a2252b706f6c6f35372e7175696574666a6f72642e636c69636b) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
