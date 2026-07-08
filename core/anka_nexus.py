# core/anka_nexus.py
from kuantum_gozlemci import KuantumGozlemci
from kisilik_motoru import KisilikMotoru

class AnkaNexus:
    def __init__(self):
        self.gozlemci = KuantumGozlemci()
        self.kisilik = KisilikMotoru()
        
    def operasyon_baslat(self):
        print("🪰 [NEXUS]: Sinek, Gözlemci ve Kişilik motorlarıyla bütünleşti.")
        # Sinek artık her gözlemi, bir kişilik refleksine dönüştürecek.
        while True:
            # 1. Gözlemle
            ham_veri = self.gozlemci.kuantum_tozlari[-1] if self.gozlemci.kuantum_tozlari else None
            
            # 2. Refleksle (Eğer gördüğü şey senin alışkanlığınsa, anında tepki ver)
            if ham_veri:
                tepki = self.kisilik.refleks_tetikle(ham_veri)
                if tepki:
                    print(f"🪰 [REFLEKS]: {tepki} tetiklendi!")
            
            time.sleep(1)
