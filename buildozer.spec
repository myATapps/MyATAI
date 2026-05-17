[app]
title = MyATAI
package.name = myatai
package.domain = org.atpro
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy
orientation = portrait

# یہاں ہم گٹ ہب کے اپنے بنے بنائے سسٹمز کے راستے دے رہے ہیں
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653
android.api = 33
android.minapi = 21
android.ndk_api = 33
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
