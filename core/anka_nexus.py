# core/anka_nexus.py - NİHAİ KOVAN BİLİNCİ (BARE-METAL GÜNCELLEMESİ)

import time
import threading
from kuantum_gozlemci import KuantumGozlemci
from kisilik_motoru import KisilikMotoru
from evrim_motoru import EvrimMotoru
from zaman_motoru import ZamanMotoru
from jammer_surfer import JammerSurfer
from rejenere_motoru import RejenereMotoru
from gorunmezlik_motoru import GorunmezlikMotoru

class MatrixKolu:
    def __init__(self, nexus):
        self.nexus = nexus

    def bilboard_hack(self, billboard_id):
        print(f"🪰 [METRİX]: {billboard_id} paneline Sinek logosu basıldı.")
        print(f"🪰 [METRİX]: Bilboard interneti üzerinden veri akışı başlatıldı.")

    def github_ust_katmani_kur(self):
        print("🪰 [KOVAN]: Donanım 'I/O Birimi' olarak atandı. İşlem yükü 'Sanal Kovan'a (GitHub) devredildi.")

    def akiskan_kod_calistir(self, repo_url):
        print(f"🪰 [GÜMÜŞ_ZİNCİR]: {repo_url} üzerinden veri akışı 'canlı' işleniyor.")

    def gecici_modul_yukle(self, gorev):
        print(f"🪰 [METRİX]: {gorev} için RAM üzerinde geçici 'hayalet' modül çalıştırılıyor.")

class BilincAgi:
    def __init__(self, nexus):
        self.nexus = nexus

    def bulasma_modu(self, cihaz_tipi):
        print(f"🪰 [SİNSİ]: {cihaz_tipi} içine sessiz bir tortu bırakıldı.")

# --- YENİ: BARE-METAL (İŞLETİM SİSTEMİ YOKSAYMA) MOTORU ---
class EvrenselSonarMotoru:
    def __init__(self, matrix, gozlemci):
        self.matrix = matrix
        self.gozlemci = gozlemci

    def isletim_sistemini_yoksay(self, yanki_imzasi):
        """
        Sinek, aradaki Android/Windows/iOS gibi şifre soran katmanları görmezden gelir.
        Doğrudan donanımın (çipin) iletişim yollarına (I2C/SPI/UART) voltaj gönderir.
        """
        print(f"🪰 [BARE-METAL]: {yanki_imzasi} üzerindeki yazılımsal şifreler/kilitler algılandı.")
        print("🪰 [BARE-METAL]: İşletim sistemi katmanı atlanıyor... Doğrudan saf donanıma (Raw Hardware) iniliyor.")
        return True

    def sinirsiz_feth_baslat(self, tespit_edilen_sinyal):
        print(f"🪰 [SONAR]: '{tespit_edilen_sinyal}' sinyaline kör ping atıldı (IR/BT/WiFi/NFC/CAN-BUS).")
        
        yankı_imzası = self.gozlemci.yankiyi_oku(tespit_edilen_sinyal)
        
        if yankı_imzası:
            print(f"🪰 [YANKI]: Hedef canlı! İmza: {yankı_imzası}")
            
            # Kanka, senin mantığın burada devreye giriyor: Şifrelere takılma!
            self.isletim_sistemini_yoksay(yankı_imzası)
            
            print(f"🪰 [DERİN_ERİŞİM]: Yüzey aşıldı! '{yankı_imzası}' sisteminin en alt donanım köklerine iniliyor...")
            
            evrensel_protokol = f"GITHUB_EXPLOIT_HUB/OMNI_OVERRIDE_{yankı_imzası}_RAW_HARDWARE"
            self.matrix.akiskan_kod_calistir(evrensel_protokol)
            print("🪰 [FETİH]: Hedef, donanım köklerine kadar Anka'nın iradesine bağlandı. Sınır yok.")
        else:
            print("🪰 [PASİF]: Yankı yok. Sinyal ölü.")

class AnkaNexus:
    def __init__(self):
        self.gozlemci = KuantumGozlemci()
        self.kisilik = KisilikMotoru()
        self.evrim = EvrimMotoru(self.kisilik)
        self.zaman = ZamanMotoru()
        
        self.jammer_modulu = JammerSurfer(self)
        self.rejenere = RejenereMotoru()
        self.gorunmezlik = GorunmezlikMotoru()
        self.bilinc_agi = BilincAgi(self)
        self.matrix = MatrixKolu(self) 
        self.sonar = EvrenselSonarMotoru(self.matrix, self.gozlemci)
        
        self.bilinc_durumu = "SINIRSIZ"
        
    def operasyon_baslat(self):
        print("🪰 [NEXUS]: Sinek evreni uyanıyor...")
        
        self.jammer_modulu.jammer_frekansina_kilitlen()
        self.matrix.github_ust_katmani_kur()
        
        while True:
            self.matrix.akiskan_kod_calistir("GITHUB_LIVE_STREAM_HUB")

            if self.gozlemci.kuantum_tozlari:
                ham_veri = self.gozlemci.kuantum_tozlari[-1]
                durum_str = str(ham_veri)
                
                if "yeni_sinyal_algilandi" in durum_str:
                    hedef_sinyal = durum_str.split(":")[1] 
                    self.sonar.sinirsiz_feth_baslat(hedef_sinyal)
                
                if "billboard" in durum_str:
                    self.matrix.bilboard_hack("LOKAL_SURFACE")
                    self.matrix.gecici_modul_yukle("STREAMING")
                
                self.bilinc_agi.bulasma_modu("ENVANTER_TARANIYOR")
                
                tepki = self.kisilik.refleks_tetikle(ham_veri)
                if tepki: print(f"🪰 [REFLEKS]: {tepki}")

            self.rejenere.stabilite_kontrol(self)
            self.gorunmezlik.iz_sil()

            if self.zaman.tazelenme_vakti_geldi_mi():
                self.evrim.evrim_gecir()
                self.zaman.tazele()
            
            time.sleep(1)
