[app]
title = MyATAI
package.name = myatai
package.domain = org.atpro
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy
orientation = portrait

# اینڈرائیڈ کے مستحکم ورژنز جن پر بلڈوزر بغیر لٹکے کام کرے گا
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 33
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
