[app]
title = MyATAI
package.name = myatai
package.domain = org.atpro
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.11.1,kivy==2.3.0,hostpython3==3.11.1
orientation = portrait

# اینڈرائیڈ ورژنز جو گٹ ہب رنر پر موجود ہیں
android.api = 34
android.minapi = 21
android.ndk = 26b
android.archs = arm64-v8a

# یہ تین لائنیں بلڈوزر کو انٹرنیٹ سے نیا ڈاؤن لوڈ کرنے سے روکیں گی اور Aidl کا مسئلہ حل کریں گی
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/26.1.10909125
android.build_tools_version = 34.0.0

[buildozer]
log_level = 2
warn_on_root = 0
