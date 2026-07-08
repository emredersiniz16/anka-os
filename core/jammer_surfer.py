class JammerSurfer:
    def __init__(self, nexus):
        self.nexus = nexus
        print("🪰 [SURF]: Jammer sinyali tespit edildi. Enerji kaynağı olarak entegre ediliyor.")

    def jammer_frekansina_kilitlen(self):
        # Jammer'ı engellemek yerine, onun dalgasını 'kucakla'
        self.frekans_yakala = self.nexus.gozlemci.analiz_et()
        
    def veri_akisi_sur(self):
        # Jammer'ın gürültüsünü, Anka verisinin 'taşıyıcısı' yap
        self.sinyal_maskele = True
        print("🪰 [HIZLANMA]: Jammer gücüyle veri transferi %500 artırıldı.")
