# simulator/anka_orchestrator.py

# Yeni eklenen Elçi (Connector) importları
from services.flight_api import FlightConnector
from services.payment_api import PaymentConnector

class AnkaOrchestrator:
    def __init__(self):
        # Elçileri atıyoruz
        self.flight_service = FlightConnector()
        self.pay_service = PaymentConnector()

    def process_command(self, raw_text):
        print(f"\n🧠 [ANKA CORE]: Emri parçalıyorum...")
        
        # 1. Uçuş Ajanı Entegrasyonu
        if "bilet" in raw_text or "fransa" in raw_text:
            print("✈️ [FLIGHT AGENT]: Uçuş verileri çekiliyor...")
            flight_data = self.flight_service.search("Paris", "20:00")
            print(f"✅ [FLIGHT]: {flight_data['flight_number']} bulundu: {flight_data['price']}")
            
            # 2. Ödeme Ajanı Entegrasyonu (Uçuş bulunduğu an tetiklenir)
            print("\n💳 [PAY AGENT]: Ödeme köprüsü kuruluyor...")
            token = self.pay_service.generate_virtual_card(flight_data['price'])
            print(f"✨ [PAYMENT]: İşlem onayına hazır: {token}")

        if not any(k in raw_text for k in ["bilet", "fransa"]):
            print("❌ [ANKA CORE]: Ajanlar meşgul veya komut belirsiz.")
            return

        print("\n✨ [SYSTEM]: İrade uygulandı, işlemler tamamlandı.")

import time

class SubAgent:
    def __init__(self, name):
        self.name = name

    def execute_task(self, detail):
        print(f"🤖 [{self.name.upper()} AGENT]: GÖREV BAŞLADI -> '{detail}' işleniyor...")
        time.sleep(0.8)
        print(f"✅ [{self.name.upper()} AGENT]: GÖREV TAMAMLANDI.")
        return True

class AnkaOrchestrator:
    def __init__(self):
        # Arkadaki görünmez ajan ordusu
        self.agents = {
            "flight": SubAgent("Flight & Travel"),
            "logistic": SubAgent("Logistic & Ride"),
            "pay": SubAgent("Anka Pay")
        }

    def process_command(self, raw_text):
        print(f"\n🧠 [ANKA CORE]: Doğal dil analiz ediliyor...")
        print(f"💬 Gelen Emir: \"{raw_text}\"")
        time.sleep(0.5)

        # Basit NLP / Niyet analizi simülasyonu
        tasks_to_trigger = []

        if "bilet" in raw_text or "fransa" in raw_text:
            tasks_to_trigger.append(("flight", "Paris 20:00 uçuşlarını tara ve en uygun olanı rezerve et"))
        
        if "araç" in raw_text or "araba" in raw_text:
            tasks_to_trigger.append(("logistic", "Havalimanından otele transfer için yerel araç bağla"))

        if "bilet kes" in raw_text or "öde" in raw_text:
            tasks_to_trigger.append(("pay", "Biyometrik onay alındığı an tek kullanımlık şifreli token üret"))

        if not tasks_to_trigger:
            print("❌ [ANKA CORE]: Emir anlaşılamadı. Lütfen tekrar deneyin.")
            return

        print(f"⚡ [ORCHESTRATOR]: {len(tasks_to_trigger)} farklı otonom ajan devreye sokuluyor...\n")
        
        # Ajanların orkestra halinde çalışması
        for agent_key, task_detail in tasks_to_trigger:
            if agent_key in self.agents:
                self.agents[agent_key].execute_task(task_detail)
                print("-" * 40)
        
        print("\n✨ [SYSTEM]: Tüm arka plan süreçleri uygulamasız ve reklamsız olarak başarıyla tamamlandı.")

if __name__ == "__main__":
    orchestrator = AnkaOrchestrator()
    # Senin o efsane örnek cümle kanka:
    user_voice_input = "Bana Fransa bileti bak Paris e saat akşam 8 e bilet kes araç ayarla"
    orchestrator.process_command(user_voice_input)
