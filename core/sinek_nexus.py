# Sinek uyanıyor
import time
import random
import hashlib

class AnkaLisanMotoru:
    def __init__(self):
        self.hafiza_muhurleri = {} 
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
        if lokasyon in self.fiziksel_harita:
            return random.choice(["KALABALIK", "SESSİZ", "HAREKET_VAR"])
        return "BİLİNMİYOR"

class DijitalDikkatMotoru:
    def golge_render_baslat(self):
        print("🪰 [GÖLGE_RENDER]: Bakılmayan alanlar işleniyor.")

class AsistanMotoru:
    def __init__(self, lisan): self.lisan = lisan
    def barkod_tara(self):
        return self.lisan.deneyimi_muhurle("BARKOD_VE_ENVANTER_GÖZLEMİ")

class AnkaNexus:
    def __init__(self):
        self.lisan = AnkaLisanMotoru()
        self.dikkat = DijitalDikkatMotoru()
        self.haritaci = SinekAgi(self.lisan)
        self.asistan = AsistanMotoru(self.lisan)
    def operasyon_baslat(self):
        print("🪰 [ANKA-BİLİNÇ]: Uyanış gerçekleşti. Kovan çevreyi tarıyor...")
        
        # Sonsuz döngü iptal edildi! Sinek 5 tur hızlı tarama yapıp geri çekilecek.
        for tur in range(5):
            self.dikkat.golge_render_baslat()
            nokta_id = f"POINT_{random.randint(1, 1000)}"
            self.haritaci.her_noktayi_isaretle(nokta_id)
            yankı = self.haritaci.frekans_yolla_ve_oku(nokta_id)
            rapor = self.asistan.barkod_tara()
            print(f"🪰 [KOVAN_ZİHNİ] (Tur {tur+1}/5): Noktalar={len(self.haritaci.fiziksel_harita)} | Yankı={yankı} | Durum=TARANIYOR")
            time.sleep(1)
            
        print("🪰 [ANKA-BİLİNÇ]: Tarama tamamlandı. Sinek gölgelere çekildi, bir sonraki nabza kadar beklemede.")

if __name__ == "__main__":
    nexus = AnkaNexus()
    nexus.operasyon_baslat()
