import platform
import sys
import time

def loading_animation(text):
    for i in range(3):
        print(f"\r{text}{'.' * (i+1)}", end="")
        time.sleep(0.4)
    print("\r" + " " * (len(text) + 5), end="\r")

arch = platform.architecture()[0]

print("\n🔍 Checking system architecture", end="")
loading_animation("")

if arch == "64bit":
    print("✅ 64-bit system detected!\n")
    time.sleep(0.5)
    print("🚀 Launching module", end="")
    loading_animation("")
    try:
        import FREE
        print("✨ Module loaded successfully!")
    except ImportError:
        print("❌ Module 'FREE' not found!")
else:
    print("\n⚠️  32-bit system detected!")
    time.sleep(0.5)
    print("❌ This program supports only 64-bit systems.")
    sys.exit()
