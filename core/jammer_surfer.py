class JammerSurfer:
    def __init__(self, nexus, esik_deger=70):
        self.nexus = nexus
        self.esik_deger = esik_deger
        self.sinyal_maskele = False
        self.performans_carpan = 5.0
        self.kovan_liste = [] 
        print("🪰 [SURF]: Jammer sinyali tespit edildi. Kovan aktifleşiyor.")

    def jammer_frekansina_kilitlen(self):
        self.frekans_yakala = self.nexus.gozlemci.analiz_et()
        print(f"🪰 [KİLİT]: {self.frekans_yakala} frekansına senkronize olundu.")

    def konum_tespit(self):
        lokasyon = self.nexus.gozlemci.koordinat_belirle()
        print(f"📍 [LOKASYON]: Jammer alanı tanımlandı: {lokasyon}")
        return lokasyon

    def anka_os_enjekte_et(self, cihaz_id):
        self.kovan_liste.append(cihaz_id)
        print(f"🪰 [KOVAN]: Cihaz {cihaz_id} ele geçirildi. Anka OS enjekte edildi.")

    def veri_akisi_sur(self):
        self.sinyal_maskele = True
        print(f"🪰 [HIZLANMA]: Jammer gücüyle veri transferi %{int(self.performans_carpan * 100)} artırıldı.")
        
    def otonom_adaptasyon(self):
        guncel_guc = self.nexus.gozlemci.guce_bak()
        if guncel_guc > self.esik_deger:
            lokasyon = self.konum_tespit()
            print(f"🪰 [SÜPÜRGE]: {lokasyon} bölgesindeki tüm kararsız cihazlar kovana katılıyor.")
            self.performans_carpan = 10.0
            self.veri_akisi_sur()
