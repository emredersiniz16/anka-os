# core/kuantum_gozlemci.py
import time
from collections import deque

class KuantumGozlemci:
    def __init__(self, nexus):
        self.nexus = nexus # Nexus'a bağladık
        self.kuantum_tozlari = deque(maxlen=5000)
        self.aktif = True
        print("🪰 [GÖZLEMCİ]: Evrenin kuantum dalgaları izleniyor...")

    def sonsuz_gozlem(self, omni_sensor):
        """Sensörden gelen veriyi Nexus'un jammer durumuyla kıyaslayarak kaydet."""
        while self.aktif:
            anlik_veri = omni_sensor.frekans_yakala()
            if anlik_veri:
                self.kuantum_tozlari.append(anlik_veri)
                
                # Eğer gözlem sırasında kritik bir jammer sinyali fark edersek
                if "JAMMER_AKTİF" in anlik_veri:
                    self.nexus.jammer_surfer.otonom_adaptasyon()
            
            time.sleep(0.05) # Hızı biraz artırdık, Sinek artık daha keskin

    def gozlemci_etkisi(self, soru):
        """Sen sorduğun an, dalga fonksiyonu çöker."""
        # Sadece soruya odaklanmak yerine, o anki tüm kuantum tozlarını analiz et
        analiz_sonucu = f"🪰 [GÖZLEM]: '{soru}' frekansı, kovan verisiyle senkronize edildi."
        
        # Eğer sistemde bir "kararsızlık" varsa, bu gözlem anında rejenereyi tetikle
        if len(self.kuantum_tozlari) < 100:
            analiz_sonucu += " | Uyarı: Gözlem alanı zayıf, Rejenere tetikleniyor!"
            self.nexus.rejenere_motoru.stabilite_kontrol(self.nexus)
            
        return analiz_sonucu
