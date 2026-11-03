# 📊 نتایج استخراج: (آخرین بروزرسانی: 08:48 12-08-1405)



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
| 1 | `tassian.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tassian.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `lolo89.larchmere.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lolo89.larchmere.xyz&port=443&secret=ee24c8636b7e946779a023ee708370719b6c6f6c6f38392e6c617263686d6572652e78797a) |
| 3 | `www.manazinjamiram.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.manazinjamiram.ir&port=8443&secret=3WMho4GHSV36xZoDAiDCXY4AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 4 | `cdn1.graduat.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn1.graduat.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `iro.varfootball2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iro.varfootball2.co.uk&port=2053&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `play.goole.com.craj.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=play.goole.com.craj.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 7 | `tim.pd.mi.v6.mgi.5s.n.p.wu.basketbalo.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tim.pd.mi.v6.mgi.5s.n.p.wu.basketbalo.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `45.136.7.187` | `2095` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.136.7.187&port=2095&secret=ee00bb3b90e49cc4abd4ed38178f8bc01b7777772e636c6f7564666c6172652e636f6d) |
| 9 | `sarzamin.mosbatbashim.info` | `2882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sarzamin.mosbatbashim.info&port=2882&secret=dd10400103324995b07c030386e886e7f1) |
| 10 | `soheil.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soheil.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `fast.proxynet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.proxynet.tech&port=443&secret=ee08787a2b7fd3220d9d35679aab082cab666173742e70726f78796e65742e74656368) |
| 12 | `mami99.birchquay.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mami99.birchquay.xyz&port=443&secret=ee920a4026fcc79354d87c30db9280e5786d616d6939392e6269726368717561792e78797a) |
| 13 | `www.hosinjon.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.hosinjon.ir&port=8443&secret=3RYDAQIAAQAB_AMDhuJMOt0AAq5W5G55ZWt0YW5ldC5jb21mYXJheqF2LmNvbXZhbi5uYWp2YS5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 14 | `s7n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s7n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `mio.foltmeingop.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mio.foltmeingop.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | `Tond.strobox.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Tond.strobox.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 17 | `66.42.63.47` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=66.42.63.47&port=8443&secret=2adab36179e7a39026adf74034615248) |
| 18 | `pofak.mikhay.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pofak.mikhay.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 19 | `joje.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=joje.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `nfc.neo-duo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nfc.neo-duo.co.uk&port=8443&secret=EERighJJvXrFGRMCIMJdCQ) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
