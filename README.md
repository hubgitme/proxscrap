# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:50 07-09-1405)



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
| 1 | `41.hide.7y76y.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=41.hide.7y76y.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `server63.esantion.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server63.esantion.info&port=2020&secret=00000000000000000000000000000000) |
| 3 | `5.222.17.103` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.17.103&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `yek.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yek.anotelinopalk.co.uk&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `91.98.97.225` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.97.225&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 6 | `37.49.229.43` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.49.229.43&port=8443&secret=dd71889eb517157210d61df330a5f11d95) |
| 7 | `orbit.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=orbit.telehelp.top&port=443&secret=eeca42440ff53ac80d54a90cdad584e47f64726976652e676f6f676c652e636f6d) |
| 8 | `ir-ourmainland.fourie.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ourmainland.fourie.co.uk&port=8443&secret=104462821249bd7ac519130220c8dd09) |
| 9 | `face-to-face.dablecheckz.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=face-to-face.dablecheckz.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 10 | `fast.prxtg.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.prxtg.top&port=443&secret=ee2c6cbde6f1e8947d8495ea1de476fc0b64726976652e676f6f676c652e636f6d) |
| 11 | `tech.gooodrat.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tech.gooodrat.co.uk&port=2096&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 12 | `server3.esantion.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server3.esantion.info&port=2020&secret=00000000000000000000000000000000) |
| 13 | `87.248.144.50` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.50&port=2083&secret=79e344818749bd7ac519130220c25d09) |
| 14 | `87.248.129.53` | `15` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.53&port=15&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 15 | `5.222.20.225` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.20.225&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `russia.knox-proxy.world` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=russia.knox-proxy.world&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `digi.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.golgoli2.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 18 | `razo11.kelpmoor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=razo11.kelpmoor.xyz&port=8443&secret=eeebf9726b89cc8ca940357d833f491a04706574726f766963682e7275) |
| 19 | `chat.appnormoor.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chat.appnormoor.info&port=443&secret=dd27729feca8dbcd8008c3fa4f12d92793) |
| 20 | `87.248.144.153` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.153&port=8880&secret=dd79e344818749bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
