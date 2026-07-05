import time
import sys
import os

# simulator klasöründeki beyni botun içine ithal ediyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from simulator.anka_orchestrator import AnkaOrchestrator

class AnkaTelegramBot:
    def __init__(self):
        self.orchestrator = AnkaOrchestrator()
        self.is_listening = False

    def handle_message(self, user_id, message_text):
        print(f"\n📥 [TELEGRAM BOT]: {user_id} kullanıcısından mesaj geldi.")
        clean_text = message_text.strip()

        # Tetikleyici kelime kontrolü ("Click" veya "Anka")
        if not self.is_listening:
            if clean_text.lower() in ["click", "anka"]:
                self.is_listening = True
                print("🪰  [BOT AUDIO]: Bzzz... *CLICK*")
                return "✨ [ANKA OS]: Dinliyorum kanka... Uygulamasız evrene hoş geldin. Emirlerini yardırabilirsin."
            else:
                return "💤 [ANKA OS]: Sistem uyku modunda. Uyandırmak için 'Click' veya 'Anka' yazın."

        # Eğer sistem zaten uyanıksa ve kullanıcı kapatmak istiyorsa
        if clean_text.lower() in ["uyku moduna geç", "sistemi kapat"]:
            self.is_listening = False
            return "🪰  [ANKA OS]: Bzzz... *CLICK* -> Sistem uzaktan uyku moduna alındı."

        # Kullanıcı uyandırdıktan sonra o efsane Fransa bileti gibi karmaşık emri verirse:
        print(f"🚀 [BOT LINK]: Emir çekirdeğe gönderiliyor...")
        result = self.orchestrator.process_command(clean_text)
        return result

# Botu Başlatma ve Hata Yönetimi
if __name__ == "__main__":
    # Render üzerinde 409 hatasını engellemek için önce web hook'ları temizle
    # Eğer telebot kütüphanesini kullanıyorsan buraya import edip
    # bot.remove_webhook() yazman gerekir.
    
    print("[=== ANKA TELEGRAM BOT SIMULATOR ACTIVE ===]")
    bot = AnkaTelegramBot()
    
    # Testler
    print(bot.handle_message("EmreBurak", "Bana bilet bak"))
    print("-" * 50)
    print(bot.handle_message("EmreBurak", "Anka"))
    print("-" * 50)
    massive_command = "Bana Fransa bileti bak Paris e saat akşam 8 e bilet kes araç ayarla"
    print(bot.handle_message("EmreBurak", massive_command))
