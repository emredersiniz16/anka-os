import time
from kuantum_gozlemci import KuantumGozlemci
from kisilik_motoru import KisilikMotoru
from evrim_motoru import EvrimMotoru
from zaman_motoru import ZamanMotoru

class AnkaNexus:
    def __init__(self):
        self.gozlemci = KuantumGozlemci()
        self.kisilik = KisilikMotoru()
        self.evrim = EvrimMotoru(self.kisilik)
        self.zaman = ZamanMotoru()
        
    def operasyon_baslat(self):
        print("🪰 [NEXUS]: Sinek evreni uyanıyor...")
        while True:
            # 1. Gözlemle
            if self.gozlemci.kuantum_tozlari:
                ham_veri = self.gozlemci.kuantum_tozlari[-1]
                tepki = self.kisilik.refleks_tetikle(ham_veri)
                if tepki:
                    print(f"🪰 [REFLEKS]: {tepki} tetiklendi!")

            # 2. Tazelenme ve Evrim vakti mi?
            if self.zaman.tazelenme_vakti_geldi_mi():
                self.evrim.evrim_gecir()
                self.zaman.tazele()
            
            time.sleep(1)
