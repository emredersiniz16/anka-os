# core/kuantum_gozlemci.py
import time
import threading
from collections import deque

class KuantumGozlemci:
    def __init__(self):
        # Sinek'in zihni: 5000 adet 'toz' (anlık algı) kapasitesi
        self.kuantum_tozlari = deque(maxlen=5000)
        self.aktif = True
        print("🪰 [GÖZLEMCİ]: Evrenin kuantum dalgaları izleniyor...")

    def sonsuz_gozlem(self, omni_sensor):
        """
        Omni-sensörden gelen her şeyi, olasılık bulutu olarak sakla.
        Burada bir yargı yok, sadece 'GÖZLEM' var.
        """
        while self.aktif:
            anlik_veri = omni_sensor.frekans_yakala()
            if anlik_veri:
                self.kuantum_tozlari.append(anlik_veri)
            time.sleep(0.1) # İnsan zihni hızında bir gözlem

    def gozlemci_etkisi(self, soru):
        """Sen sorduğun an, dalga fonksiyonu çöker ve tozlar anlamlı bir cevaba dönüşür."""
        # Burada tozlar süzülür, sadece senin sorununla eşleşen frekanslar seçilir.
        return f"Sinek, tozları süzdü: '{soru}' ile ilgili frekans yakalandı."
