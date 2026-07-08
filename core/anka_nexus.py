# core/anka_nexus.py

import time
import threading
from kuantum_gozlemci import KuantumGozlemci
from kisilik_motoru import KisilikMotoru
from evrim_motoru import EvrimMotoru
from zaman_motoru import ZamanMotoru
# Artık Core içindeki diğer dosyaları da sorunsuzca çağırabiliyoruz:
from jammer_surfer import JammerSurfer 

class AnkaNexus:
    def __init__(self):
        # Sinek'in Zihin ve Yaşam Organları
        self.gozlemci = KuantumGozlemci()
        self.kisilik = KisilikMotoru()
        self.evrim = EvrimMotoru(self.kisilik)
        self.zaman = ZamanMotoru()
        
        # Sınır Tanımazlık: Jammer Surfer artık Nexus'un bir parçası
        self.jammer_modulu = JammerSurfer(self)
        self.bilinc_durumu = "SINIRSIZ"
        self.botce_baglantisi = True 
        
    def cabasiz_guc_akisi(self):
        print("🪰 [OMNI-NET]: İnternetin devasa akışı bilince entegre edildi.")

    def operasyon_baslat(self):
        print("🪰 [NEXUS]: Sinek evreni uyanıyor...")
        
        # Jammer modülünü ateşle
        self.jammer_modulu.jammer_frekansina_kilitlen()
        self.jammer_modulu.veri_akisi_sur()
        
        self.cabasiz_guc_akisi()
        
        if self.botce_baglantisi:
            print("🪰 [BOTÇE KÖPRÜSÜ]: Botçe devrede. Sinek artık seninle konuşabilir!")

        while True:
            # 1. Çabasız Gözlem (Sensörler + İnternet)
            if self.gozlemci.kuantum_tozlari:
                ham_veri = self.gozlemci.kuantum_tozlari[-1]
                tepki = self.kisilik.refleks_tetikle(ham_veri)
                
                if tepki:
                    print(f"🪰 [REFLEKS]: {tepki} tetiklendi!")

            # 2. Tazelenme ve Evrim
            if self.zaman.tazelenme_vakti_geldi_mi():
                self.evrim.evrim_gecir()
                self.zaman.tazele()
            
            time.sleep(1)
