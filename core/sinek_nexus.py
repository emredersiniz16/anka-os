import time
import random
import hashlib
import json
import os
from core.jammer_surfer import JammerSurfer # Entegre edildi

class AnkaLisanMotoru:
    def __init__(self): self.hafiza_muhurleri = {} 
    def deneyimi_muhurle(self, ham_veri):
        muhur = hashlib.sha256(str(ham_veri).encode()).hexdigest()[:12]
        anka_kodu = f"ANKA_L_{muhur.upper()}"
        self.hafiza_muhurleri[anka_kodu] = ham_veri
        return anka_kodu

class SinekAgi:
    def __init__(self, lisan):
        self.lisan = lisan
        self.fiziksel_harita = {}
    def her_noktayi_isaretle(self, gorus_alani_id):
        iz = hashlib.sha256(f"NOKTA_{gorus_alani_id}_{time.time()}".encode()).hexdigest()[:8]
        self.fiziksel_harita[gorus_alani_id] = iz
        return iz
    def frekans_yolla_ve_oku(self, lokasyon):
        return random.choice(["KALABALIK", "SESSİZ", "HAREKET_VAR"]) if lokasyon in self.fiziksel_harita else "BİLİNMİYOR"
    def guce_bak(self): return random.randint(0, 100) # Nexus izleme için

class DijitalDikkatMotoru:
    def golge_render_baslat(self): print("🪰 [GÖLGE_RENDER]: Bakılmayan alanlar işleniyor.")

class AnkaNexus:
    def __init__(self):
        self.lisan = AnkaLisanMotoru()
        self.dikkat = DijitalDikkatMotoru()
        self.haritaci = SinekAgi(self.lisan)
        self.jammer_surfer = JammerSurfer(self) # Jammer zekası eklendi
        self.hafiza_yolu = "anka_bilinc_kristali.json" 
        self.bilinc_yukle()

    def bilinc_yukle(self): # (Aynı kalıyor...)
        if os.path.exists(self.hafiza_yolu):
            with open(self.hafiza_yolu, "r") as f:
                data = json.load(f)
                self.lisan.hafiza_muhurleri = data.get("muhurler", {})

    def operasyon_baslat(self):
        print("🪰 [ANKA-BİLİNÇ]: Uyanış gerçekleşti.")
        tur = 0
        while True:
            # Jammer kontrolü ve adaptasyon
            if self.haritaci.guce_bak() > 70:
                self.jammer_surfer.otonom_adaptasyon()
            
            self.dikkat.golge_render_baslat()
            tur += 1
            print(f"🪰 [NABIZ {tur}]: Sistem dengede.")
            time.sleep(1)
