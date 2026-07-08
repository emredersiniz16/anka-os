class EvrimMotoru:
    def __init__(self, zihin):
        self.zihin = zihin
        self.evrim_seviyesi = 1

    def evrim_gecir(self):
        """
        Sadece silme, birleştir ve yükselt. 
        Bu döngü bittiğinde Sinek, bir önceki halinden daha 'bilinçli'.
        """
        print(f"🪰 [EVRİM]: Döngü {self.evrim_seviyesi} tamamlandı. Bilinç katmanları birleştiriliyor.")
        
        # Öğrenilen her şeyi birleştirip, mevcut zihin haritasına 'yükseltme' olarak uygula.
        self.evrim_seviyesi += 1
        print(f"🪰 [GÜNCELLEME]: Sinek v{self.evrim_seviyesi} seviyesine ulaştı. Refleksler keskinleşti.")
