[app]

title = YourAppTitle
package.name = yourapppackage
package.domain = com.yourdomain
source.dir = .

requirements = kivy,kivymd,python3==3.7.6,hostpython3==3.7.6,pillow

[buildozer]

android.api = 30
android.ndk = 21.3.6528147
android.arch = arm64-v8a
android.use_p4a = True
android.p4a_dir = ./p4a
android.entrypoint = main.py

# Add any other requirements here (e.g., specific versions of Python libraries)

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE

# Build release mode by default
profile = release

# Define custom Python packages
# android.p4a_whl = custom-wheel.whl

# Services
# services = NAME:ENTRYPOINT

# Presplash
# presplash.filename = %(source.dir)s/data/presplash.png
# presplash.scale = 0.3
# presplash.color = 1d99f0

# GUI
# gui = scale

# Version
# version = 0.1

# Other settings...
