# simulator/anka_orchestrator.py
import time
from services.flight_api import FlightConnector
from services.payment_api import PaymentConnector

class AnkaOrchestrator:
    def __init__(self):
        # Elçileri (Services) atıyoruz
        self.flight_service = FlightConnector()
        self.pay_service = PaymentConnector()

    def process_command(self, raw_text):
        response_buffer = [] 
        response_buffer.append("🧠 [ANKA CORE]: Emri parçalıyorum...")
        
        # 1. Uçuş ve Lojistik Ajanı Entegrasyonu
        if "bilet" in raw_text or "fransa" in raw_text:
            response_buffer.append("✈️ [FLIGHT AGENT]: Uçuş verileri çekiliyor...")
            flight_data = self.flight_service.search("Paris", "20:00")
            response_buffer.append(f"✅ [FLIGHT]: {flight_data['flight_number']} bulundu: {flight_data['price']}")
            
            # 2. Ödeme Ajanı Entegrasyonu
            response_buffer.append("💳 [PAY AGENT]: Ödeme köprüsü kuruluyor...")
            token = self.pay_service.generate_virtual_card(flight_data['price'])
            response_buffer.append(f"✨ [PAYMENT]: İşlem onayına hazır: {token}")

        if "araç" in raw_text:
            response_buffer.append("🚗 [LOGISTIC AGENT]: Havalimanı transferi için araç bağlandı.")

        if not any(k in raw_text for k in ["bilet", "fransa", "araç"]):
            response_buffer.append("❌ [ANKA CORE]: Ajanlar meşgul veya komut belirsiz.")
            
        response_buffer.append("\n✨ [SYSTEM]: İrade uygulandı, işlemler tamamlandı.")
        
        # Botun Telegram'a basması için metni döndürüyoruz
        return "\n".join(response_buffer)

if __name__ == "__main__":
    # Test için
    orchestrator = AnkaOrchestrator()
    print(orchestrator.process_command("Bana Fransa bileti bak ve araç ayarla"))
