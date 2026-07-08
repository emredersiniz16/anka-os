# core/zaman_motoru.py
import time

class ZamanMotoru:
    def __init__(self, taze_kalma_suresi=3600):
        # Sinek'in evreni taze tutma süresi (varsayılan 1 saat)
        self.taze_kalma_suresi = taze_kalma_suresi 
        self.baslangic_zamani = time.time()
        print(f"🪰 [ZAMAN]: Evrensel döngü başlatıldı. Tazelenme süresi: {taze_kalma_suresi}s")

    def tazelenme_vakti_geldi_mi(self):
        # Eğer süre dolduysa, sistemi "Sıfırlama Modu"na (Hafızaya mühürleme) çek
        gecen_sure = time.time() - self.baslangic_zamani
        return gecen_sure >= self.taze_kalma_suresi

    def tazele(self):
        print("🪰 [TAZELEME]: Matris sönümleniyor, tortu (bilinç) mühürleniyor...")
        self.baslangic_zamani = time.time()
