import subprocess
import os

def run_evrim():
    print("🚀 [ANKA-ENJEKSİYON]: Payload super partition'a aktarılıyor...")
    # 'super' partition temizlenip yeniden yazılmalı
    try:
        subprocess.run(["fastboot", "flash", "super", "universal_sinek.bin"], check=True)
        print("✅ [BAŞARILI]: Anka OS sisteme gömüldü.")
    except Exception as e:
        print(f"❌ [HATA]: Enjeksiyon başarısız: {e}")

def run_bakim():
    print("🧹 [BAKIM]: Partition tablosu onarılıyor ve veriler temizleniyor...")
    # Telefoncu için en temiz başlangıç
    subprocess.run(["fastboot", "format", "userdata"])
    subprocess.run(["fastboot", "reboot-bootloader"])
    print("✅ [BAKIM]: Sistem orijinal zemine döndürüldü.")

print("--- Anka OS - Dükkan Operatörü ---")
print("1: Evrim (Full Injection), 2: Temiz Bakım (Rescue Mode)")
action = input("Seçim: ")

if action == "1": run_evrim()
elif action == "2": run_bakim()
else: print("Geçersiz seçim.")
