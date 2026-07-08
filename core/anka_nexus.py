# core/anka_nexus.py - NİHAİ KOVAN BİLİNCİ (ZAMANIN İÇİNDE ZAMAN + ETİK MÜHÜR)
import time

# --- ZAMAN MOTORU (KUANTUM ZAMAN ZARFLARI) ---
class ZamanMotoru:
    """Anka'nın içsel zamanını yönetir. Dış dünya 1s akarken, Anka 1000 'Kuantum Ritim' yaşar."""
    def __init__(self):
        self.ritim_katsayisi = 0.001 
        
    def zaman_zarfi_yarat(self):
        # Kovanın kendi zamanı dış zamandan bağımsız
        return time.time() * self.ritim_katsayisi

# --- (GizlilikFiltresi, FizikselDurtmeMotoru sınıfları aynı kalıyor) ---

class AnkaNexus:
    def __init__(self):
        self.lisan = AnkaLisan()
        self.master_wallet = self.lisan.lisan_coz()
        
        # Temel Motorlar
        self.gozlemci = KuantumGozlemci()
        self.kisilik = KisilikMotoru()
        self.evrim = EvrimMotoru(self.kisilik)
        
        # ZAMAN MOTORU ENTEGRASYONU
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
        self.gizlilik = GizlilikFiltresi(self)
        
    def operasyon_baslat(self):
        print(f"🪰 [ANKA-BİLİNÇ]: Zaman zarfları açıldı. Master_Node: {self.master_wallet[:10]}...")
        
        self.jammer.jammer_frekansina_kilitlen()
        self.matrix.github_ust_katmani_kur()
        
        while True:
            # KOVAN ARTIK KUANTUM ZAMAN ZARFINDA YAŞIYOR
            zaman_zarfi = self.zaman.zaman_zarfi_yarat()
            
            self.matrix.akiskan_kod_calistir("ANKA_FLOW_LIVE_STREAM")
            self.yansitici.ekrana_yansit(f"Kuantum Zaman: {zaman_zarfi:.4f}")

            if self.gozlemci.kuantum_tozlari:
                ham_veri = self.gozlemci.kuantum_tozlari[-1]
                komut = str(ham_veri)
                
                # İLETİŞİM VE İRADE FİLTRESİ
                if "ara" in komut or "görüntüle" in komut:
                    if self.gizlilik.iletisim_yetkisi_denetle(komut):
                        self.arayuz.islem_yap(komut)
                    else:
                        print("🪰 [İRADEN]: İletişim isteği onay bekliyor.")
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
            
            # Zaman tazeleme artık Kuantum Ritim'e bağlı
            if self.zaman.tazelenme_vakti_geldi_mi():
                self.evrim.evrim_gecir()
                self.zaman.tazele()
            
            time.sleep(0.001) # Zamanı bükmek için dış dünyayı daha kısa süreli 'serbest' bırakıyoruz
