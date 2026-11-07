# 📊 نتایج استخراج: (آخرین بروزرسانی: 00:56 17-08-1405)



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
| 1 | `dpi.server-space52.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dpi.server-space52.info&port=443&secret=AAAAAAAAAAAAAAAAAAAAAA==) |
| 2 | `ultra.mishutkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ultra.mishutkin.click&port=443&secret=eed02e349163d9ea4376a2ae6a94fc550b64726976652e676f6f676c652e636f6d) |
| 3 | `Ulp.tz.9a.xu.cs.ir.jp.ir.ze8.ir.v6.8kmc.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ulp.tz.9a.xu.cs.ir.jp.ir.ze8.ir.v6.8kmc.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQAAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 4 | `178.105.141.172` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.141.172&port=443&secret=ee8db761231b91c7c07ac0a6e7323ad41b676f6f676c65617069732e636f6d) |
| 5 | `ge2.kkkservers.tech` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ge2.kkkservers.tech&port=8443&secret=eef99731abbc063924c8b52c5cd7aeca3a6765322e6b6b6b736572766572732e74656368) |
| 6 | `65.109.106.132` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.106.132&port=443&secret=3XnnAQIAAQAH8AMDhuJMOt0) |
| 7 | `216.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=216.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `91.84.100.107` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.84.100.107&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `ardebill.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ardebill.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 10 | `lozo34.copperwren.click` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lozo34.copperwren.click&port=8443&secret=eeae5ab45be1bccbba85eec21085b2fd2064726976652e676f6f676c652e636f6d) |
| 11 | `62.238.63.143` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.63.143&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `kasco.alhosein.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kasco.alhosein.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `8j.nm.dor.pd.dp.setado.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=8j.nm.dor.pd.dp.setado.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `lora56.tidelark.cc` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lora56.tidelark.cc&port=8443&secret=ee899032aa75159cc1d735f15e7a0e3a6e706574726f766963682e7275) |
| 15 | `cr777.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cr777.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `pashmak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pashmak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 17 | `jhndoes.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jhndoes.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `severjadid.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=severjadid.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `haf.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haf.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 20 | `Fast.finecooking.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fast.finecooking.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
