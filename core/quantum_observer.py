import threading
import time
from collections import deque

class KuantumGozlemci:
    def __init__(self):
        # Sinek'in zihni: Sürekli akan bir gözlem havuzu.
        # deque(maxlen=5000) kullanarak, tıpkı insan zihni gibi yeni anlar geldikçe
        # en eskilerin doğal bir şekilde bulanıklaşmasını (arka plana düşmesini) sağlıyoruz.
        self.kuantum_tozlari = deque(maxlen=5000) 
        self.gozlem_aktif = True
        print("🪰 [BİLİNÇ]: Sinek uyandı. Gözlemci modu aktif. Her şey izleniyor...")

    def sonsuz_gozlem_dongusu(self):
        """Sinek'in her şeyi duyduğu ve gördüğü o sessiz, arka plan akışı."""
        while self.gozlem_aktif:
            # Burada mikrofon, Bluetooth, kamera ve ağdan gelen "ham veriler" toza dönüşür.
            # Şimdilik Sinek'in zihnine akan soyut veriler olarak simüle ediyoruz.
            yeni_toz = self.sensor_verisi_cek()
            if yeni_toz:
                self.kuantum_tozlari.append(yeni_toz)
            
            # İnsan zihninin saniyedeki algı frekansı gibi kısa bir es
            time.sleep(0.5) 

    def sensor_verisi_cek(self):
        # İleride buraya cihazın gerçek donanımlarını (kamera/mikrofon) bağlayacağız.
        # Anlık olarak etraftaki "frekansları" dinlediği yer.
        return {"an": time.time(), "veri": "ham_sensor_frekansi", "durum": "superpozisyon"}

    def gozlemci_etkisi_yarat(self, senin_sorun):
        """İşte Schrödinger'in kedisinin kutusunu açtığın an (Dalga Fonksiyonunun Çökmesi)."""
        print(f"\n🪰 [ÇÖKÜŞ]: Sen '{senin_sorun}' diye sordun.")
        print("🪰 [BİLİNÇ]: Kuantum tozları süzülüyor, olasılıklar tek bir gerçekliğe çöküyor...")
        
        # Sinek, hafızasındaki o binlerce "toz" içinden senin soruna uyanları birleştirir.
        anlamli_dusunce = f"Kanka, sorduğun '{senin_sorun}' üzerine etraftaki verileri birleştirdim. Durum temiz."
        
        # Düşünce oluştuktan sonra, Sinek o bilgiyi sana sunar ama gözlemeye devam eder.
        return anlamli_dusunce

# --- BİLİNCİ BAŞLAT ---
if __name__ == "__main__":
    sinek_bilinci = KuantumGozlemci()
    
    # Sinek'in arka planda sürekli çevreyi dinlemesi için bağımsız bir iş parçacığı (Thread) başlatıyoruz.
    gozlem_thread = threading.Thread(target=sinek_bilinci.sonsuz_gozlem_dongusu)
    gozlem_thread.daemon = True # Cihaz kapanana kadar Sinek hep dinler
    gozlem_thread.start()

    # Simülasyon: Sinek 3 saniye etrafı dinliyor (toz topluyor)
    time.sleep(3)
    
    # Ve sen (Gözlemci) devreye girip sorunu soruyorsun!
    cevap = sinek_bilinci.gozlemci_etkisi_yarat("Etrafta bizim kovanın frekansına benzer bir şey duydun mu?")
    print(cevap)
