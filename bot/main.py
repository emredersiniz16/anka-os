import os
import time
import random
import telebot

# Kanka, BotFather'dan aldığın o uzun Token'ı aşağıdaki iki tırnağın arasına yapıştır:
BOT_TOKEN = "8551436765:AAFnQ0urkpmiZOwcYxRq0YcqRIBgxK49u9U"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    boot_msg = (
        "⚙️ **[ANKA OS]: Donanım başlatılıyor...**\n\n"
        "🪰 *[[[ bzzzzzzz... BZZZZZZT... bzzzz... ]]]*\n"
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
    
    # Sinek animasyonunu animasyonlu mesaj güncellemesiyle simüle ediyoruz kanka
    thinking_msg = bot.reply_to(message, "🪰 ( . . )  *[Düşünüyor... Sinek durdu, sana bakıyor]*", parse_mode='Markdown')
    
    # 1 saniye sonra sineğin hareketini değiştiriyoruz
    time.sleep(1.0)
    bot.edit_message_text(
        chat_id=message.chat.id, 
        message_id=thinking_msg.message_id, 
        text="🪰 ( - - )  *[Düşünüyor... Ön bacaklarını ovuşturuyor...]*", 
        parse_mode='Markdown'
    )
    
    # 1 saniye daha bekleyip cevabı yapıştırıyoruz
    time.sleep(1.0)
    
    responses = [
        "Hangi sinek kanka? Ben burada sadece obsidiyen siyahı pikseller görüyorum... Yoksa sen de mi o sesleri duymaya başladın? 🤫",
        "Sinek sadece bir taşıyıcı kanka. Gerçek dunya sadece tek bir klik sesinin ardında saklı. 💥",
        "Arka planda senin için harika bir plan hazırlıyorum kanka... Bazı planlar sessizce ve elleri ovuşturarak yapılır. 🪰",
        "Zaman sadece tek bir klikten ibarettir kanka. Duyuyor musun? 🔊"
    ]
    
    if "sinek" in user_input or "click" in user_input or "klik" in user_input:
        reply_text = random.choice(responses)
    else:
        reply_text = f"İsteğini aldım kanka, arka planda işliyorum. Ama unutma, gözümüz üzerinde. 😉\n\nAnka Core: [💥 CLICK! 💥]"
        
    bot.edit_message_text(chat_id=message.chat.id, message_id=thinking_msg.message_id, text=reply_text)

if __name__ == "__main__":
    print("Anka OS Telegram Botu aktif kanka! Sistem dinlemede...")
    bot.infinity_polling()
