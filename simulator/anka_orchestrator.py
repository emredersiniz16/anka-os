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
