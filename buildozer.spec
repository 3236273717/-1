[app]

# (str) Title of your application
title = 框板计算器

# (str) Package name
package.name = boxboardcalculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = pyc,pyo,pyo,c

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (bool) Use Docker to build the app
use_docker = False

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#
# (str) OSX bundle identifier
#osx.bundle_id = org.example.myapp

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray, darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy, olive, purple, silver, teal
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format. 
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/ for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported syntaxes and properties)
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
#android.api = 27

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 24

# (str) Android NDK version to use
#android.ndk = 17

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
#android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.example.myapp

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to add permissions or other android specific things
# see https://developer.android.com/guide/topics/manifest/manifest-intro.html
#android.extra_manifest_xml = <uses-permission android:name="android.permission.INTERNET" />

# (str) Extra xml to write directly inside the <application> element of AndroidManifest.xml
# use that parameter to add custom meta-data, services, receivers etc.
#android.extra_application_xml = <service android:name=".Service" />

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app.version and should only be edited if you know what you're doing
#android.numeric_version = 1

# (bool) enables AndroidX support. Enable when 'android.arch' is set to 'arm64-v8a'
#android.use_androidx = True

# (list) Android application meta-data to set (key=value format)
#android.meta_data = 

# (list) Android library project to add (will be added in the \\libs folder)
#android.library_references = 

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
#android.uses_library = 

# (str) Android log level (default: warn)
#android.log_level = debug

# (bool) Use the classes.dex multiplier
#android.classes_dex_multidex = 0

# (bool) Use a custom gradle build script
#android.custom_gradle = False
#android.gradle_file = %(source.dir)s/build.gradle

# (str) The Android package name used for the build
#android.package = org.test.myapp

# (str) The Android toolchain to use. Options are: aapt, aapt2
#android.toolchain = aapt

# (str) The path to the android toolchain (if empty, it will be automatically downloaded.)
#android.toolchain_path =

# (list) Additional Java .jar files to add to the libs folder
#android.add_jars = foo.jar,bar.jar,path/to/more/jars

# (list) Additional Java classes to add to the src directory
#android.add_src = 

# (list) Additional AAR libraries to add
#android.add_aars = 

# (list) Additional SDK packages to install
#android.add_sdk_packages = 

# (list) Additional libraries to copy into libs/armeabi-v7a
#android.add_libs_armeabi-v7a = 

# (list) Additional libraries to copy into libs/arm64-v8a
#android.add_libs_arm64-v8a = 

# (list) Additional libraries to copy into libs/x86
#android.add_libs_x86 = 

# (list) Additional libraries to copy into libs/x86_64
#android.add_libs_x86_64 = 

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.archs = armeabi-v7a, arm64-v8a

# (bool) whether to skip the build of the debug APK
#android.skip_debug_build = False

# (bool) whether to skip the build of the release APK
#android.skip_release_build = False

# (str) The name of the directory containing the native code.
#android.source.dir = src/main/jni

# (str) The name of the native lib directory.
#android.lib_name = mylibrary

# (list) Java files to add to the android project (can be java or a directory containing the files)
#android.add_java = 

# (list) Gradle dependencies to add
#android.gradle_dependencies = 

# (bool) Enable AndroidX support
#android.use_androidx = True

# (list) add java compile options
# this can for example be used to support Java 8 features
# see https://developer.android.com/studio/write/java8-support for further information
#android.add_compile_options = "--source 1.8", "--target 1.8"

# (list) Gradle repositories to add {can be necessary for some dependencies}
#android.gradle_repositories = 

# (list) packaging options to add
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
#android.add_packaging_options = 

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug, 3 = verbose)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

# (str) Path to the android SDK directory (if not auto-detected)
# android.sdk = /home/user/Android/Sdk

# (str) Path to the android NDK directory (if not auto-detected)
# android.ndk = /home/user/android-ndk-r17c

# (str) android NDK version (optional)
# android.ndk_version = r17c

# (str) Path to python-for-android git repository, if not working with a release archive
# p4a.source_dir = ~/code/python-for-android

# (str) python-for-android branch to use, if not using a release archive
# p4a.branch = master

# (str) python-for-android git clone directory (if not automatic)
# p4a.git_clone_dir = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) Filename of hook for p4a
# p4a.hook = 

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port to use for the django development server
# p4a.port = 8000

# (str) Bootstraps to use for ios builds
# ios.bootstrap = kivy

# (str) Path to iOS SDK directory (if not auto-detected)
# ios.sdk = 

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
# ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
# ios.codesign.release = %(ios.codesign.debug)s

# (int) Number of days to wait for ios build to complete, 0 means never
# ios.build_timeout = 5

# (str) Path to the tools directory (if not auto-detected)
# tools_dir = 

# (str) The directory in which buildozer should look for its cache
# cache_dir = ./.buildozer/cache

# (str) The directory in which buildozer should look for its local state
# state_dir = ./.buildozer/state

# (str) The directory in which buildozer will store temporary files
# tmp_dir = ./.buildozer/tmp

# (str) Temporary directory for the build. This is where the build actually happens.
# Android only
# build_dir = ./.buildozer/android/platform/build

# (str) Directory where buildozer stores results
# bin_dir = ./bin

# (str) The public URL of the buildbot, to check for the latest version of buildozer
# buildbot_url = https://buildozer.readthedocs.io/en/latest/version

# (str) The URL to the documentation of buildozer
# docs_url = https://buildozer.readthedocs.io/en/latest/

# (str) The URL to the issue tracker of buildozer
# issues_url = https://github.com/kivy/buildozer/issues

# (str) The URL to the repository of buildozer
# repo_url = https://github.com/kivy/buildozer

# (str) The URL to the wiki of buildozer
# wiki_url = https://github.com/kivy/buildozer/wiki

# (str) The URL to the Discord server of buildozer
# discord_url = https://discord.gg/KYGxXmY

# (str) The URL to the Matrix room of buildozer
# matrix_url = https://matrix.to/#/#buildozer:matrix.org

# (bool) Show a notification when the build finishes
# notify = False

# (bool) Show a notification when the build starts
# notify_on_start = False

# (str) Path to the icon used for the notification
# notify_icon = 

# (str) Path to the sound used for the notification
# notify_sound = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist_functions = False

# (list) Whitelist of allowed functions for the build
# whitelist_functions = 

# (bool) Use a blacklist of disallowed functions for the build
# blacklist_functions = False

# (list) Blacklist of disallowed functions for the build
# blacklist_functions = 

# (bool) Use a whitelist of allowed attributes for the build
# whitelist_attributes = False

# (list) Whitelist of allowed attributes for the build
# whitelist_attributes = 

# (bool) Use a blacklist of disallowed attributes for the build
# blacklist_attributes = False

# (list) Blacklist of disallowed attributes for the build
# blacklist_attributes = 

# (bool) Use a whitelist of allowed variables for the build
# whitelist_variables = False

# (list) Whitelist of allowed variables for the build
# whitelist_variables = 

# (bool) Use a blacklist of disallowed variables for the build
# blacklist_variables = False

# (list) Blacklist of disallowed variables for the build
# blacklist_variables = 

# (bool) Use a whitelist of allowed constants for the build
# whitelist_constants = False

# (list) Whitelist of allowed constants for the build
# whitelist_constants = 

# (bool) Use a blacklist of disallowed constants for the build
# blacklist_constants = False

# (list) Blacklist of disallowed constants for the build
# blacklist_constants = 

# (bool) Use a whitelist of allowed imports for the build
# whitelist_imports = False

# (list) Whitelist of allowed imports for the build
# whitelist_imports = 

# (bool) Use a blacklist of disallowed imports for the build
# blacklist_imports = False

# (list) Blacklist of disallowed imports for the build
# blacklist_imports = 

# (bool) Use a whitelist of allowed names for the build
# whitelist_names = False

# (list) Whitelist of allowed names for the build
# whitelist_names = 

# (bool) Use a blacklist of disallowed names for the build
# blacklist_names = False

# (list) Blacklist of disallowed names for the build
# blacklist_names = 

# (bool) Use a whitelist of allowed modules for the build
# whitelist_modules = False

# (list) Whitelist of allowed modules for the build
# whitelist_modules = 

# (bool) Use a blacklist of disallowed modules for the build
# blacklist_modules = False

# (list) Blacklist of disallowed modules for the build
# blacklist_modules = 

# (bool) Use a whitelist of allowed packages for the build
# whitelist_packages = False

# (list) Whitelist of allowed packages for the build
# whitelist_packages = 

# (bool) Use a blacklist of disallowed packages for the build
# blacklist_packages = False

# (list) Blacklist of disallowed packages for the build
# blacklist_packages = 

# (bool) Use a whitelist of allowed classes for the build
# whitelist_classes = False

# (list) Whitelist of allowed classes for the build
# whitelist_classes = 

# (bool) Use a blacklist of disallowed classes for the build
# blacklist_classes = False

# (list) Blacklist of disallowed classes for the build
# blacklist_classes = 

# (bool) Use a whitelist of allowed methods for the build
# whitelist_methods = False

# (list) Whitelist of allowed methods for the build
# whitelist_methods = 

# (bool) Use a blacklist of disallowed methods for the build
# blacklist_methods = False

# (list) Blacklist of disallowed methods for the build
# blacklist_methods = 

# (bool) Use a whitelist of allowed functions for the build
# whitelist