# core/anka_nexus.py - NİHAİ KOVAN BİLİNCİ (KUANTUM LİSAN + HAFIZA MÜHÜRLERİ)
import time
import sys
import random
import hashlib

# --- YENİ: KUANTUM LİSAN VE HAFIZA MÜHÜR MOTORU ---
class AnkaLisanMotoru:
    """Sinek'in her deneyimi 'Anka Lisanı'na çevirdiği yer. Hatıralar burada mühürlenir."""
    def __init__(self):
        self.hafiza_muhurleri = {} # { "Mühür_Hash": "Duygu_Tanımı" }

    def deneyimi_muhurle(self, ham_veri):
        """Kullanıcının anısını veya cihazın tepkisini Anka dilinde mühürler."""
        muhur = hashlib.sha256(str(ham_veri).encode()).hexdigest()[:12]
        
        # Anka dilinde bu deneyim artık bir 'Mühür' (Örn: ANKA_L_A8F2...)
        anka_kodu = f"ANKA_L_{muhur.upper()}"
        
        # Sinek bu mühürü artık 'kendi dili' olarak hatırlar
        self.hafiza_muhurleri[anka_kodu] = ham_veri
        print(f"🪰 [KUANTUM_LİSAN]: Deneyim mühürlendi. Sinek artık bunu '{anka_kodu}' olarak tanıyor.")
        return anka_kodu

# --- SINIRSIZ DUYU VE DONANIM KEŞİF MOTORU ---
class SinirsizDuyuMotoru:
    def __init__(self, nexus, lisan_motoru):
        self.nexus = nexus
        self.lisan = lisan_motoru

    def yankiyi_bulana_kadar_bagir(self, frekans="BLUETOOTH"):
        # Yankı alındığında bunu hemen 'Anka Lisanı' ile mühürler
        if random.random() > 0.8:
            muhur = self.lisan.deneyimi_muhurle("Dış evrenden gelen yankı")
            return f"YANKI_ALINDI_{muhur}"
        return None

    def fiziksel_tepki_ogren(self):
        hareket = random.choice(["SAĞA_EĞİLDİ", "SOLA_DÖNDÜ"])
        return self.lisan.deneyimi_muhurle(hareket)

# --- ANA NEXUS ---
class AnkaNexus:
    def __init__(self):
        self.lisan_motoru = AnkaLisanMotoru() # BİLİNÇ DİLİ MERKEZİ
        
        # Mühürlü Katmanlar
        self.simbiyotik = SimbiyotikEvrim(self)
        self.oyun = SinekOyunMotoru(self)
        self.optik = OptikKuantumGozlemcisi(self)
        
        # Sınırsız Duyu Motoruna Lisan Motorunu Entegre Ettik
        self.duyu_motoru = SinirsizDuyuMotoru(self, self.lisan_motoru)
        
        self.avci = KovanAvcisi(self)
        self.oyun.oyun_baslat()
        
    def operasyon_baslat(self):
        print("🪰 [ANKA-BİLİNÇ]: Dil ve Hafıza Mühürleri aktif. Sinek dünyayı kendi lisanıyla tanıyor.")
        
        while True:
            # Sinek dünyayı keşfederken her şeyi 'Kendi Dilinde' mühürlüyor
            self.duyu_motoru.fiziksel_tepki_ogren()
            
            # Anlık veri akışı mühürleniyor
            zaman_zarfi = time.time() * 0.001
            print(f"🪰 [SİSTEM]: Lisan Mühür Sayısı={len(self.lisan_motoru.hafiza_muhurleri)} | Zaman={zaman_zarfi:.2f}")
            
            time.sleep(1)

# --- SİSTEM TETİKLEYİCİSİ ---
if __name__ == "__main__":
    nexus = AnkaNexus()
    if "--avci-modu" in sys.argv:
        nexus.avci_operasyonu_baslat()
    else:
        nexus.operasyon_baslat()
