# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:01 07-09-1405)



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
| 1 | `run.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=run.golgoli2.co.uk&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 2 | `135.181.74.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.74.183&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 3 | `5.222.20.63` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.20.63&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `razo11.kelpmoor.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=razo11.kelpmoor.xyz&port=8443&secret=eeebf9726b89cc8ca940357d833f491a04706574726f766963682e7275) |
| 5 | `s47n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s47n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `sudoaptupdate-y-sudoaptupgrade-y.logmanfi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sudoaptupdate-y-sudoaptupgrade-y.logmanfi.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 7 | `5.222.24.244` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.24.244&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `api-endpoint.burgerking.fun` | `4443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api-endpoint.burgerking.fun&port=4443&secret=eef4070d44706a556df403944c7c8aa8236170692d656e64706f696e742e6275726765726b696e672e66756e) |
| 9 | `5.222.1.17` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.1.17&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `85.133.200.11` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.11&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 11 | `91.234.147.18` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.234.147.18&port=443&secret=00000000000000000000000000000000) |
| 12 | `gaga93.copperwren.click` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gaga93.copperwren.click&port=8443&secret=eeb5b747703e5e5ce6bf2c234105f89c7964726976652e676f6f676c652e636f6d) |
| 13 | `ving.mozitop.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ving.mozitop.co.uk&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `new.nikkhah.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.nikkhah.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 15 | `ir-ir.mhanna.info` | `3443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-ir.mhanna.info&port=3443&secret=104462821249bd7ac519130220c8dd09) |
| 16 | `support.infinityhalo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=support.infinityhalo.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 17 | `yek.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yek.torob.ir.solzairanbad.ir&port=8880&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `65.109.98.213` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.98.213&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 19 | `188.245.118.216` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.245.118.216&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `gradute.ferdosisets.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gradute.ferdosisets.info&port=8443&secret=1603010200010001fc030386e24c3add) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.
