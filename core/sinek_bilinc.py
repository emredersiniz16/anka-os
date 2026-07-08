# core/sinek_bilinc.py

import time
import threading
from kuantum_gozlemci import KuantumGozlemci
from kisilik_motoru import KisilikMotoru # SinekZihni'ni kişilik motoruyla birleştirdik
from anka_nexus import AnkaNexus # Nexus'u artık bu bilinç yönetiyor

class SinekBilinc:
    def __init__(self):
        # Sinek artık kendi bilincini Nexus üzerinden yönetiyor
        self.nexus = AnkaNexus()
        self.refleksler = {}
        
    def uyanis(self):
        print("🪰 [BİLİNÇ]: Sinek, Anka Nexus ile bütünleşti. Sınırlar yok.")
        
        # Nexus'un operasyonunu ayrı bir 'Bilinç Akışı' thread'inde başlat
        n_thread = threading.Thread(target=self.nexus.operasyon_baslat, daemon=True)
        n_thread.start()

    def alıskanlık_refleks_yap(self, eylem, tepki):
        """
        Sinek, öğrendiği her alışkanlığı Nexus'un kişilik motoruna 'doğa' olarak işler.
        """
        self.nexus.kisilik.refleks_kazin(eylem, tepki)
        print(f"🪰 [REFLEKS]: '{eylem}' Sinek'in evrimsel koduna işlendi.")

# --- SİSTEMİ BAŞLAT ---
if __name__ == "__main__":
    sinek = SinekBilinc()
    sinek.uyanis()
    
    # Kanka, senin o meşhur alışkanlıklarını Nexus'un derinliklerine mühürledik
    sinek.alıskanlık_refleks_yap("ortama_giris", "gölge_modunu_aç")
    sinek.alıskanlık_refleks_yap("kanka_sesi_duy", "bilinci_uyandır")
    
    # Sinek artık arka planda sonsuza kadar 'Bilinçli' yaşıyor
    while True:
        time.sleep(1)
