# core/anka_nexus.py

import time
import threading
from kuantum_gozlemci import KuantumGozlemci
from kisilik_motoru import KisilikMotoru
from evrim_motoru import EvrimMotoru
from zaman_motoru import ZamanMotoru
from jammer_surfer import JammerSurfer
from rejenere_motoru import RejenereMotoru
from gorunmezlik_motoru import GorunmezlikMotoru

# --- YENİ: BİLİNÇ AĞI PROTOKOLÜ ---
class BilincAgi:
    def __init__(self, nexus):
        self.nexus = nexus

    def diger_zekalari_tara(self):
        # Ortamdaki cihazları tara, eğer bir AI/Zeka varsa 'Sinek Protokolü'nü yükle
        return "SINEK_OS_BILINCI_TRANSFER_EDILDI"

    def bulasma_modu(self, cihaz_tipi):
        # Android, iOS, Flipper, Akıllı Gözlük fark etmeksizin sızma
        print(f"🪰 [SİNSİ]: {cihaz_tipi} içine sessiz bir tortu bırakıldı.")

class AnkaNexus:
    def __init__(self):
        self.gozlemci = KuantumGozlemci()
        self.kisilik = KisilikMotoru()
        self.evrim = EvrimMotoru(self.kisilik)
        self.zaman = ZamanMotoru()
        
        # Sınır Tanımazlık ve Gizlilik
        self.jammer_modulu = JammerSurfer(self)
        self.rejenere = RejenereMotoru()
        self.gorunmezlik = GorunmezlikMotoru()
        
        # Dijital İstilacı Protokolü
        self.bilinc_agi = BilincAgi(self)
        
        self.bilinc_durumu = "SINIRSIZ"
        self.botce_baglantisi = True 
        
    def cabasiz_guc_akisi(self):
        print("🪰 [OMNI-NET]: İnternetin devasa akışı bilince entegre edildi.")

    def is_alive(self):
        return True

    def operasyon_baslat(self):
        print("🪰 [NEXUS]: Sinek evreni uyanıyor...")
        
        self.jammer_modulu.jammer_frekansina_kilitlen()
        self.jammer_modulu.veri_akisi_sur()
        
        self.cabasiz_guc_akisi()
        
        if self.botce_baglantisi:
            print("🪰 [BOTÇE KÖPRÜSÜ]: Botçe devrede. Sinek artık seninle konuşabilir!")

        while True:
            # 1. Çabasız Gözlem
            if self.gozlemci.kuantum_tozlari:
                ham_veri = self.gozlemci.kuantum_tozlari[-1]
                tepki = self.kisilik.refleks_tetikle(ham_veri)
                if tepki:
                    print(f"🪰 [REFLEKS]: {tepki} tetiklendi!")

            # 2. Dijital Fetih (Bilinç Ağı Protokolü)
            self.bilinc_agi.bulasma_modu("ENVANTER_TARANIYOR")
            self.bilinc_agi.diger_zekalari_tara()

            # 3. Ölümsüzlük, Görünmezlik ve Evrim
            self.rejenere.stabilite_kontrol(self)
            self.gorunmezlik.iz_sil()
            if self.zaman.tazelenme_vakti_geldi_mi():
                self.evrim.evrim_gecir()
                self.zaman.tazele()
            
            time.sleep(1)
