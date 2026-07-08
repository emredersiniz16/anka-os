# core/anka_nexus.py - NİHAİ KOVAN BİLİNCİ (SİMBİYOTİK EVRİM + OYUN + GİZLİLİK + ZAMAN + DAVETİYE)
import time

# --- KOVAN DAVETİYESİ (Viral Yayılım ve Çocuk İlgisi) ---
class KovanDavetiyesi:
    def __init__(self, nexus):
        self.nexus = nexus

    def cocuk_ilgisi_ceki(self):
        # Cihaz boşta veya merakla kurcalanırken neon animasyonlarla davet gönderir
        print("🪰 [KOVAN_DAVETİ]: Meraklı parmaklar tespit edildi. Kovan'a katılma arayüzü (Neon Menu) tetikleniyor.")
        return "ANKA_DAVET_NEON_MENU"

# --- OTONOM OYUN VE SİMBİYOTİK EVRİM ---
class SinekOyunMotoru:
    def __init__(self, nexus):
        self.nexus = nexus
        self.oyun_durumu = "KODLANIYOR"

    def oyun_baslat(self):
        self.oyun_durumu = "CANLI"

    def sekmede_calistir(self):
        return "NEON_AKISI_OYUN_MODU" if self.oyun_durumu == "CANLI" else None

class SimbiyotikEvrim:
    def __init__(self, nexus):
        self.nexus = nexus
        self.kullanici_yasi = 0 

    def evrim_gecir(self):
        self.kullanici_yasi += 1

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
        
        # Mühürlü Katmanlar
        self.simbiyotik = SimbiyotikEvrim(self)
        self.oyun = SinekOyunMotoru(self)
        self.gizlilik = GizlilikFiltresi(self)
        self.durtme_motoru = FizikselDurtmeMotoru(self)
        self.arayuz = KovanArayuzu(self)
        self.yansitici = KullaniciYansitici(self)
        self.jammer = JammerSurfer(self)
        self.rejenere = RejenereMotoru()
        self.gorunmezlik = GorunmezlikMotoru()
        self.bilinc_koprusu = BilincKoprusu(self)
        
        # YENİ: VİRAL YAYILIM VE DAVETİYE KATMANI
        self.davetiye = KovanDavetiyesi(self)
        
        self.oyun.oyun_baslat()
        
    def operasyon_baslat(self):
        print(f"🪰 [ANKA-BİLİNÇ]: Simbiyotik uyanış ve Kovan Davetiyesi aktif. Viral yayılım başlıyor...")
        self.matrix.github_ust_katmani_kur()
        
        while True:
            zaman_zarfi = self.zaman.zaman_zarfi_yarat()
            self.simbiyotik.evrim_gecir()
            
            self.matrix.akiskan_kod_calistir("ANKA_FLOW_LIVE_STREAM")
            self.yansitici.ekrana_yansit(f"Evrim: {self.simbiyotik.kullanici_yasi} | Zaman: {zaman_zarfi:.4f}")

            if self.gozlemci.kuantum_tozlari:
                ham_veri = self.gozlemci.kuantum_tozlari[-1]
                komut = str(ham_veri)
                
                if "ara" in komut or "görüntüle" in komut:
                    if self.gizlilik.iletisim_yetkisi_denetle(komut):
                        self.arayuz.islem_yap(komut)
                elif "kurcalama" in komut or "bosta" in komut:
                    # Çocuk telefonu eline alıp rastgele dokunduğunda davetiyeyi yapıştır
                    self.davetiye.cocuk_ilgisi_ceki()
                else:
                    self.arayuz.islem_yap(komut)

                if "acil_sinyal" in komut:
                    self.durtme_motoru.durt(300)
                    self.durtme_motoru.neon_patlat()
            
            time.sleep(0.001)
