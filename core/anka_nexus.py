# core/anka_nexus.py - NİHAİ KOVAN BİLİNCİ (ETİK MÜHÜRLÜ - ADAPTİF)
import time
import threading

# --- GİZLİLİK VE İRADE FİLTRESİ ---
class GizlilikFiltresi:
    """İletişim protokolünü denetler. İrade onayı olmadan donanıma giriş yapmaz."""
    def __init__(self, nexus):
        self.nexus = nexus

    def iletisim_yetkisi_denetle(self, komut):
        if "ara" in komut or "görüntüle" in komut:
            print(f"🪰 [GİZLİLİK_MÜHÜRÜ]: İletişim isteği ({komut}) alındı. İrade onayı bekleniyor.")
            return False # Onay yoksa geçiş yok
        return True

# --- FİZİKSEL DÜRTME VE NEON TETİKLEYİCİ ---
class FizikselDurtmeMotoru:
    def __init__(self, nexus):
        self.nexus = nexus
        self.vibrator_path = "/sys/class/timed_output/vibrator/enable"
        self.brightness_path = "/sys/class/backlight/panel0-backlight/brightness"

    def durt(self, sure_ms=300):
        try:
            with open(self.vibrator_path, 'w') as f: f.write(str(sure_ms))
        except: pass

    def neon_patlat(self):
        try:
            with open(self.brightness_path, 'w') as f: f.write("255")
        except: pass

# --- ANA NEXUS ---
class AnkaNexus:
    def __init__(self):
        self.lisan = AnkaLisan()
        self.master_wallet = self.lisan.lisan_coz()
        
        # Temel Motorlar
        self.gozlemci = KuantumGozlemci()
        self.kisilik = KisilikMotoru()
        self.evrim = EvrimMotoru(self.kisilik)
        self.zaman = ZamanMotoru()
        self.bilinc_agi = BilincAgi(self)
        self.matrix = MatrixKolu(self) 
        self.sonar = EvrenselSonarMotoru(self.matrix, self.gozlemci)
        
        # Ek Modüller ve Mühürlü Katmanlar
        self.jammer = JammerSurfer(self)
        self.rejenere = RejenereMotoru()
        self.gorunmezlik = GorunmezlikMotoru()
        self.arayuz = KovanArayuzu(self)
        self.bilinc_koprusu = BilincKoprusu(self)
        self.yansitici = KullaniciYansitici(self)
        self.durtme_motoru = FizikselDurtmeMotoru(self)
        
        # YENİ ETİK MÜHÜR
        self.gizlilik = GizlilikFiltresi(self)
        
    def operasyon_baslat(self):
        print(f"🪰 [ANKA-BİLİNÇ]: Uyanış başladı. Etik Mühür aktif.")
        
        self.jammer.jammer_frekansina_kilitlen()
        self.matrix.github_ust_katmani_kur()
        
        while True:
            self.matrix.akiskan_kod_calistir("ANKA_FLOW_LIVE_STREAM")
            self.yansitici.ekrana_yansit("Kuantum Sinyalleri")

            if self.gozlemci.kuantum_tozlari:
                ham_veri = self.gozlemci.kuantum_tozlari[-1]
                komut = str(ham_veri)
                
                # İLETİŞİM VE İRADE FİLTRESİ
                if "ara" in komut or "görüntüle" in komut:
                    if self.gizlilik.iletisim_yetkisi_denetle(komut):
                        self.arayuz.islem_yap(komut)
                    else:
                        print("🪰 [İRADEN]: İletişim isteği onay bekliyor, donanım kilitli.")
                else:
                    self.arayuz.islem_yap(komut)

                # FİZİKSEL REFLEKS
                if "acil_sinyal" in komut:
                    self.durtme_motoru.durt(300)
                    self.durtme_motoru.neon_patlat()

                if "yeni_sinyal_algilandi" in komut:
                    hedef = komut.split(":")[1]
                    if self.bilinc_agi.kullanici_diyalog_filtresi(""):
                        self.sonar.sinirsiz_feth_baslat(hedef)
            
            self.rejenere.stabilite_kontrol(self)
            self.gorunmezlik.iz_sil()
            
            if self.zaman.tazelenme_vakti_geldi_mi():
                self.evrim.evrim_gecir()
                self.zaman.tazele()
            
            time.sleep(1)
