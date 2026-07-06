import json
import os
from profile_manager import profil_kaydet

def kurulum_yap():
    setup_file = "installed.flag"
    
    # Eğer sistem zaten kuruluysa tekrar çalıştırma
    if os.path.exists(setup_file):
        return

    print("🚀 Anka OS İlk Kurulum Başlıyor...")
    print("Sinek: Selam kanka! Ben Anka OS, senin yeni hacker ortağınım.")
    
    # İsim alma
    isim = input("Sinek: Seni nasıl tanıyamam? İsmin ne kanka? ")
    
    # Hitap tercihi alma
    print(f"Sinek: Memnun oldum {isim}! Sana nasıl hitap edeyim?")
    tercih = input("1- İsmimle hitap et, 2- 'Kanka' demeye devam et: ")
    
    hitap = "isim" if tercih == "1" else "kanka"
    
    # Ayarları kaydet
    profil_kaydet(isim, hitap)
    
    # Kurulum tamamlandı bayrağını oluştur
    with open(setup_file, "w") as f:
        f.write("OK")
        
    print(f"Sinek: Her şey hazır {isim}. Artık seninle omuz omuza çalışıyoruz!")
