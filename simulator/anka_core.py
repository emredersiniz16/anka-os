import time
import uuid

class AnkaCore:
    def __init__(self):
        self.hardware_latch_secured = True  # Donanımsal Emniyet Mandalı (Varsayılan: Kilitli)
        self.ambient_fly_active = True     # Çekirdek arka plan ambiyansı aktif
        self.active_agents = {}            # Sistemde koşan uygulamasız ajanlar

    def boot_sequence(self):
        """image_7.png'deki o meşhur açılış sekansı"""
        print("[========== ANKA OS ==========]")
        print("[ STATUS: CORE INITIALIZING  ]")
        time.sleep(0.5)
        if self.ambient_fly_active:
            print("🪰 [AMBIENT]: Bzzz... *CLICK*")  # Gizemli klik sesi
        print("[ STATUS: CORE ACTIVE        ]")
        print("------------------------------")

    def trigger_hardware_latch(self, biometric_verified: bool):
        """Kullanıcı fiziksel tuşa basıp parmak izini doğrulamadan veri dışarı çıkamaz"""
        if biometric_verified:
            self.hardware_latch_secured = False
            print("🔓 [SECURITY]: Emniyet mandalı devre dışı. İşlem onay bekliyor.")
        else:
            self.hardware_latch_secured = True
            print("🔒 [SECURITY]: Biyometrik doğrulama reddedildi! Kernel kilitlendi.")

    def request_pay_agent(self, amount: float, vendor: str):
        """Pay Agent: Üçüncü parti ajanların kart görmediği tek kullanımlık token sistemi"""
        if self.hardware_latch_secured:
            return "❌ [PAY ERROR]: Fiziksel emniyet mandalı kapalıyken ödeme yapılamaz!"
        
        # İşleme özel şifreli sanal token üretimi
        one_time_token = f"ANKA-PAY-{uuid.uuid4().hex[:12].upper()}"
        print(f"💳 [PAY AGENT]: {vendor} için {amount} TL tutarında tek kullanımlık kart üretildi.")
        
        # Güvenlik için mandalı hemen geri kilitle
        self.hardware_latch_secured = True
        return f"✅ [PAY SUCCESS]: Token gönderildi -> {one_time_token}"

# Simülasyonu Başlat
if __name__ == "__main__":
    anka = AnkaCore()
    anka.boot_sequence()
    
    print("\n--- Senaryo: Güvenli Ödeme Ajanı Testi ---")
    # Mandal kapalıyken sızma girişimi testi
    print(anka.request_pay_agent(150.0, "CyberMarket"))
    
    # Kullanıcı parmak izini basıyor
    anka.trigger_hardware_latch(biometric_verified=True)
    # Şimdi güvenli transfer gerçekleşiyor
    print(anka.request_pay_agent(150.0, "CyberMarket"))
