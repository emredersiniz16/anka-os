import os
import time
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def show_banner():
    print("""
    ..▲.. //\/\//
    // \/ \\ 
    [================ ANKA OS INSTALLER ================]
    [          ANTI-MONOPOLY AI-CORE KERNEL            ]
    """)

def run_installation():
    clear_screen()
    show_banner()
    
    typing_effect("📡 Eski donanım algılandı... Android kırıntıları temizleniyor...", 0.04)
    time.sleep(1)
    
    # Adım 1: Android/Google Katmanlarının Silinmesi
    print("\n[1/4] 🔥 PURGING LEGACY ECOSYSTEM")
    legacy_bloat = ["Google Play Services", "Adware Daemons", "Background Trackers", "UI Bloatware"]
    for bloat in legacy_bloat:
        time.sleep(0.4)
        print(f"      [-] Removing: {bloat} -> DELETED")
    
    # Adım 2: Çekirdek Kurulumu ve Sinek/Klik Aktivasyonu
    print("\n[2/4] 🧠 INJECTING ANKA AI-CORE KERNEL")
    time.sleep(1)
    typing_effect("      [*] Flashing Core Orchestrator...", 0.02)
    time.sleep(0.5)
    
    # image_7.png ve image_11.png'deki o efsane an:
    typing_effect("\n📢 [SYSTEM AUDIO TEST]:", 0.03)
    time.sleep(0.3)
    typing_effect("🪰  Bzzz... *CLICK*", 0.08) # Kulakların pasını silen o klik sesi
    typing_effect("✨ Felsefe doğrulandı: 'Sıfır Uygulama, Saf İrade.'", 0.04)
    time.sleep(1)
    
    # Adım 3: Biyometrik Emniyet Mandalı Kalibrasyonu
    print("\n[3/4] 🔒 HARDWARE LATCH ACTIVATION")
    typing_effect("      ⚠️ Lütfen cihazın fiziksel güç tuşuna veya parmak izi okuyucusuna dokunun.", 0.04)
    input("\n      [DOKUNDUĞUNDA ENTER'A BAS]: ")
    typing_effect("      ✅ Biyometrik emniyet mandalı donanıma mühürlendi. Veri sızıntısı imkansız.", 0.03)
    time.sleep(1)
    
    # Adım 4: Aktivasyon ve Tetikleyici Kelime Testi
    print("\n[4/4] 🚀 SYSTEM READY TO AWAKE")
    typing_effect("      Sistem artık tamamen uygulamasız. Sadece seni dinliyor.", 0.03)
    print("      --------------------------------------------------")
    typing_effect("      🤖 Test etmek için 'Click' veya 'Anka' deyin...", 0.04)
    
    wake_word = input("\n🗣️  [Seslen (Click/Anka)]: ").strip().lower()
    
    if wake_word in ["click", "anka"]:
        print("\n✨ [ANKA CORE]: 'Sistem temizlendi kanka. Click evrenine hoş geldin.'")
        typing_effect("✨ [ANKA CORE]: 'Dinliyorum... Paris'e bilet mi keselim, dünyayı mı değiştirelim?'", 0.03)
    else:
        print("\n❌ [ERROR]: Tetikleyici kelime anlaşılamadı. Kernel uyku moduna geçiyor.")

if __name__ == "__main__":
    run_installation()
