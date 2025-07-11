[app]
title = RPG Épico
package.name = rpgepico
package.domain = com.rpgepico

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3

version = 1.0.0
requirements = python3,kivy,plyer

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 21b
android.sdk = 30
android.accept_sdk_license = True
