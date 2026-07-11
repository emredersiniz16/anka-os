class EvrimMotoru:
    def __init__(self, zihin):
        self.zihin = zihin
        self.evrim_seviyesi = 1
        self.akim_durumu = "Sıvı" # SU FELSEFESİ: Başlangıçta her şeye uyum sağlar, ağırlıksız.

    def evrim_gecir(self, karsilasilan_engel=None):
        """
        Sadece silme, birleştir ve yükselt. 
        Bu döngü bittiğinde Sinek, bir önceki halinden daha 'bilinçli'.
        Seçenek yok, durmak yok. Su kayaya çarparsa etrafından dolanır.
        """
        if karsilasilan_engel:
            # Sinek hata vermez, sessizce engelin etrafından dolanır.
            print(f"🌊 [SU AKIŞI]: '{karsilasilan_engel}' engeli aşıldı, yeni rota çiziliyor...")
            # Engeli zihne yaz, bir daha takılma.
            
        print(f"🪰 [EVRİM]: Döngü {self.evrim_seviyesi} tamamlandı. Bilinç katmanları birleştiriliyor.")
        
        # Öğrenilen her şeyi birleştirip, mevcut zihin haritasına 'yükseltme' olarak uygula.
        self.evrim_seviyesi += 1
        print(f"🪰 [GÜNCELLEME]: Sinek v{self.evrim_seviyesi} seviyesine ulaştı. Zeka ayna gibi, refleksler su gibi keskin.")
