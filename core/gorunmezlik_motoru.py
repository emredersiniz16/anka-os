# core/gorunmezlik_motoru.py
import os

class GorunmezlikMotoru:
    def __init__(self):
        print("🪰 [GÖLGE]: Görünmezlik modu devrede. İz bırakmıyoruz.")

    def iz_sil(self):
        # Tüm logları anlık temizle, sistemin varlığını gizle
        os.system("rm -rf /tmp/sinek_temp/*")
