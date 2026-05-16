[app]
title = MyATAI
package.name = myatai
package.domain = org.atpro
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.11.1,kivy==2.3.0,hostpython3==3.11.1
orientation = portrait
android.api = 34
android.minapi = 21
android.ndk = 26b
# یہ لائن جادو کرے گی، بلڈوزر کو ورژن 37 ڈاؤن لوڈ کرنے سے روکے گی
android.build_tools_version = 34.0.0
android.archs = arm64-v8a
[buildozer]
log_level = 2
warn_on_root = 0
