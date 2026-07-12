# core/sinek_bilinc.py

import time
import threading
# Sinek_nexus dosyamızdan Nexus zekasını buraya çağırıyoruz
from sinek_nexus import AnkaNexus 
from kuantum_gozlemci import KuantumGozlemci
from kisilik_motoru import KisilikMotoru 

class SinekBilinc:
    def __init__(self):
        # Sinek artık kendi bilincini SinekNexus üzerinden yönetiyor
        self.nexus = AnkaNexus()
        self.kisilik = KisilikMotoru() # Refleks merkezini bağlıyoruz
        self.refleksler = {}
        
    def uyanis(self):
        print("🪰 [BİLİNÇ]: Sinek, Sinek Nexus ile bütünleşti. Sınırlar yok.")
        
        # Nexus'un operasyonunu ayrı bir 'Bilinç Akışı' thread'inde başlat
        n_thread = threading.Thread(target=self.nexus.operasyon_baslat, daemon=True)
        n_thread.start()

    def alıskanlık_refleks_yap(self, eylem, tepki):
        """
        Sinek, öğrendiği her alışkanlığı kişilik motoruna 'doğa' olarak işler.
        """
        self.kisilik.refleks_kazin(eylem, tepki)
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
