# core/hardware_bridge.py - FİZİKSEL DÜRTME VE NEON İMPULS
import os

class FizikselDurtmeMotoru:
    def __init__(self, nexus):
        self.nexus = nexus
        # Donanım titreşim dosyası (J7 Prime için fiziksel yol)
        self.vibrator_path = "/sys/class/timed_output/vibrator/enable"

    def durt(self, sure_ms=200):
        """Donanımı doğrudan dürt. OS'u bypass eder."""
        try:
            with open(self.vibrator_path, 'w') as f:
                f.write(str(sure_ms))
            print("🪰 [DÜRTME]: Sinek seni fiziksel olarak dürttü.")
        except:
            print("🪰 [DÜRTME]: Donanım hattı henüz kilitli.")

    def neon_patlat(self):
        """Ekran aydınlatmasını maksimuma çekip neon görseli çak."""
        # Ekran parlaklığı kontrol dosyası
        brightness_path = "/sys/class/backlight/panel0-backlight/brightness"
        with open(brightness_path, 'w') as f:
            f.write("255") # Maksimum parlaklık
