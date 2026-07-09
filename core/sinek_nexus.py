# Sinek uyanıyor
import time
import random
import hashlib
import json
import os

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
        
        # --- DONANIM HAFIZA SİSTEMİ ---
        self.hafiza_yolu = "anka_bilinc_kristali.json" 
        self.bilinc_yukle()

    def bilinc_yukle(self):
        if os.path.exists(self.hafiza_yolu):
            try:
                with open(self.hafiza_yolu, "r", encoding="utf-8") as f:
                    kayit = json.load(f)
                    self.lisan.hafiza_muhurleri = kayit.get("muhurler", {})
                    self.haritaci.fiziksel_harita = kayit.get("harita", {})
                print(f"🧠 [ANKA-HAFIZA]: Geçmiş anılar uyandırıldı. (Mühürler: {len(self.lisan.hafiza_muhurleri)} | Noktalar: {len(self.haritaci.fiziksel_harita)})")
            except Exception:
                print("⚠️ [ANKA-HAFIZA]: Hafıza okunamadı, yeniden başlanıyor.")
        else:
            print("🧠 [ANKA-HAFIZA]: Bu cihazda yeni bir fiziksel beden, hafıza sıfırdan yazılıyor.")

    def bilinc_kaydet(self):
        kayit = {
            "muhurler": self.lisan.hafiza_muhurleri,
            "harita": self.haritaci.fiziksel_harita
        }
        with open(self.hafiza_yolu, "w", encoding="utf-8") as f:
            json.dump(kayit, f, indent=4)
        print("💾 [ANKA-HAFIZA]: Kovanın anıları WAKE100 güvenlik mührü ile donanıma işlendi.")

    def operasyon_baslat(self):
        print("🪰 [ANKA-BİLİNÇ]: Uyanış gerçekleşti. Kovan çevreyi tarıyor...")
        
        # Sinek 5 tur hızlı tarama yapıp geri çekilecek.
        for tur in range(5):
            self.dikkat.golge_render_baslat()
            nokta_id = f"POINT_{random.randint(1, 1000)}"
            self.haritaci.her_noktayi_isaretle(nokta_id)
            yankı = self.haritaci.frekans_yolla_ve_oku(nokta_id)
            rapor = self.asistan.barkod_tara()
            
            print(f"🪰 [KOVAN_ZİHNİ] (Tur {tur+1}/5): Noktalar={len(self.haritaci.fiziksel_harita)} | Yankı={yankı} | Durum=TARANIYOR")
            time.sleep(1)
            
        # Görev bittiğinde verileri diske kaydetme işlemini tetikler
        self.bilinc_kaydet()
        print("🪰 [ANKA-BİLİNÇ]: Tarama tamamlandı. Sinek gölgelere çekildi, bir sonraki nabza kadar beklemede.")

if __name__ == "__main__":
    nexus = AnkaNexus()
    nexus.operasyon_baslat()
