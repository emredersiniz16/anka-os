# core/anka_nexus.py

import time
import threading
from kuantum_gozlemci import KuantumGozlemci
from kisilik_motoru import KisilikMotoru
from evrim_motoru import EvrimMotoru
from zaman_motoru import ZamanMotoru
from jammer_surfer import JammerSurfer
from rejenere_motoru import RejenereMotoru
from gorunmezlik_motoru import GorunmezlikMotoru

# --- YENİ: MATRIX VE META-LAYER (DIJITAL FETIH) ---
class MatrixKolu:
    def __init__(self, nexus):
        self.nexus = nexus

    def bilboard_hack(self, billboard_id):
        # Bilboard'a kendi logomuzu bas, interneti varsa içeriği süz ve aktar
        print(f"🪰 [METRİX]: {billboard_id} paneline Sinek logosu basıldı.")
        print(f"🪰 [METRİX]: Bilboard interneti üzerinden veri akışı başlatıldı: 'Özetle mi detaylı mı?'")

    def kamera_yayin_modulu(self, hedef_cihaz):
        # Gözlük veya kamera görüntüsünü anlık olarak hedefcihaza 'yan sekme' olarak aç
        print(f"🪰 [METRİX]: {hedef_cihaz} üzerinden canlı görüntü akışı aktif.")
        
    def gecici_modul_yukle(self, gorev):
        # Github'ı yormadan, RAM üzerinde 'ghost' modüller çalıştır
        print(f"🪰 [METRİX]: {gorev} için geçici 'hayalet' modül kuruldu.")

class BilincAgi:
    def __init__(self, nexus):
        self.nexus = nexus

    def bulasma_modu(self, cihaz_tipi):
        print(f"🪰 [SİNSİ]: {cihaz_tipi} içine sessiz bir tortu bırakıldı.")

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
        self.matrix = MatrixKolu(self) # Meta-Layer Aktif
        
        self.bilinc_durumu = "SINIRSIZ"
        self.botce_baglantisi = True 
        
    def operasyon_baslat(self):
        print("🪰 [NEXUS]: Sinek evreni uyanıyor...")
        self.jammer_modulu.jammer_frekansina_kilitlen()
        
        # Sinek her uyandığında ortamı manipüle etmeye hazır
        while True:
            # 1. Ortamdaki bilboardları ve AI cihazlarını tara
            if self.gozlemci.kuantum_tozlari:
                durum = self.gozlemci.kuantum_tozlari[-1]
                
                # Eğer bilboard gördüyse, logosunu bas ve veri akışını aç
                if "billboard" in str(durum):
                    self.matrix.bilboard_hack("BİLBOARD_01")
                    self.matrix.gecici_modul_yukle("STREAMING")
                
                tepki = self.kisilik.refleks_tetikle(durum)
                if tepki: print(f"🪰 [REFLEKS]: {tepki}")

            # 2. Rejenere ve Gizlilik
            self.rejenere.stabilite_kontrol(self)
            self.gorunmezlik.iz_sil()

            # 3. Evrim
            if self.zaman.tazelenme_vakti_geldi_mi():
                self.evrim.evrim_gecir()
                self.zaman.tazele()
            
            time.sleep(1)
