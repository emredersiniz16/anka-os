import os
import time
import random
import sys
import telebot
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# 1. ADIM: Orkestratörü (Beyni) dahil ediyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from simulator.anka_orchestrator import AnkaOrchestrator

orchestrator = AnkaOrchestrator()

# Kanka, token'ı koda gömmüyoruz. Sunucuya yüklediğimizde arkada gizli bir anahtar olarak tanımlayacağız.
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    print("❌ HATA: BOT_TOKEN bulunamadı! Lütfen çevre değişkenini (Environment Variable) tanımla kanka.")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    boot_msg = (
        "⚙️ **[ANKA OS]: Donanım başlatılıyor...**\n\n"
        "🪰 *[[[ bzzzzzzz... BZZZZZZT... bzz... ]]]*\n"
        "...sny_09: Sinek kafesin içinde aranıyor...\n\n"
        "🔊 *>>> [💥 CLICK! 💥 ] <<<*\n"
        "[SYSTEM_INFO]: Döngü kırıldı. Eski sistem temizlendi.\n\n"
        "==========================================\n"
        "      **ANKA OS (Project Phoenix) v0.1** \n"
        "      [ CORE ACTIVE // 🌊 NEURAL WAVE ]    \n"
        "==========================================\n\n"
        "Anka Core: Sistem temizlendi kanka. Click evrenine hoş geldin.\n"
        "Bana bir komut ver veya sistemi test etmek için bir şeyler yaz..."
    )
    bot.reply_to(message, boot_msg, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_input = message.text.lower()
    
    thinking_msg = bot.reply_to(message, "🪰 ( . . )  *[Düşünüyor... Sinek durdu, sana bakıyor]*", parse_mode='Markdown')
    
    time.sleep(1.0)
    bot.edit_message_text(
        chat_id=message.chat.id, 
        message_id=thinking_msg.message_id, 
        text="🪰 ( - - )  *[Düşünüyor... Ön bacaklarını ovuşturuyor...]*", 
        parse_mode='Markdown'
    )
    
    time.sleep(1.0)
    
    if "sinek" in user_input or "click" in user_input or "klik" in user_input:
        responses = [
            "Hangi sinek kanka? Ben burada sadece obsidiyen siyahı pikseller görüyorum... Yoksa sen de mi o sesleri duymaya başladın? 🤫",
            "Sinek sadece bir taşıyıcı kanka. Gerçek dünya sadece tek bir klik sesinin ardında saklı. 💥",
            "Arka planda senin için harika bir plan hazırlıyorum kanka... Bazı planlar sessizce ve elleri ovuşturarak yapılır. 🪰",
            "Zaman sadece tek bir klikten ibarettir kanka. Duyuyor musun? 🔊"
        ]
        reply_text = random.choice(responses)
    else:
        # 2. ADIM: İŞTE BEYİN BURADA DEVREYE GİRİYOR!
        # Uçuş, araç, bilet kelimeleri gelince Orchestrator tetiklenecek.
        reply_text = orchestrator.process_command(message.text)
        
    bot.edit_message_text(chat_id=message.chat.id, message_id=thinking_msg.message_id, text=reply_text)

# Render'ı kandırmak için sahte bir web sunucusu (kalkan) yaratıyoruz
def keep_alive():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            # İŞTE KESİN ÇÖZÜM: 'b' harfini kaldırdık, .encode('utf-8') ekledik! Python artık çökmeyecek.
            self.wfile.write("Anka OS Kalkani Aktif! Sistem tikir tikir calisiyor.".encode('utf-8'))
            
    # Render'ın bize atadığı kapıyı (PORT) bul, bulamazsan 8080 yap
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()

if __name__ == "__main__":
    # Önce sahte web sunucusunu arka planda başlatıyoruz
    print("🛡️ [SYSTEM]: Render kalkani (Port) aktif ediliyor...")
    threading.Thread(target=keep_alive, daemon=True).start()
    
    # Ve asıl beynimiz, telegram botumuz uyanıyor
    print("🚀 [ANKA OS]: Telegram Botu aktif kanka! Sistem dinlemede...")
    bot.infinity_polling()
