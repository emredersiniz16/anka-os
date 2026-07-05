import time
import sys
import random

def print_glitch(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def boot_sequence():
    print_glitch("\n[ANKA OS]: Donanim baslatiliyor...", 0.03)
    time.sleep(1)
    
    print("\n🪰 [[[ bzzzzzzz... BZZZZZZT... bzzzz... ]]]")
    print_glitch("...sny_09: Sinek kafesin icinde araniyor...", 0.05)
    time.sleep(2)
    
    print("\n🔊 >>> [💥 CLICK! 💥 ] <<<")
    print_glitch("[SYSTEM_INFO]: Dongu kirildi. Eski sistem temizlendi.", 0.02)
    time.sleep(1)
    
    print("\n==========================================")
    print("      ANKA OS (Project Phoenix) v0.1      ")
    print("      [ CORE ACTIVE // 🌊 NEURAL WAVE ]    ")
    print("==========================================\n")
    print("AI Core: Sistem temizlendi kanka. Click evrenine hos geldin.\n")

def thinking_animation():
    frames = [
        "🪰 ( . . )  [Dusunuyor: Sinek durdu, sana bakiyor]",
        "🪰 ( - - )  [Dusunuyor: Ön bacaklarini ovusturuyor...]",
        "🪰 ( • • )  [Dusunuyor: Gozlerini temizliyor, sinsi bir plan yapiyor]"
    ]
    print_glitch("\n🌊 [Ses dalgasi buzuluyor, sinek formuna geciyor...]", 0.02)
    for _ in range(2):
        for frame in frames:
            sys.stdout.write(f"\r{frame}")
            sys.stdout.flush()
            time.sleep(1.0)
    print("\n🔊 >>> [💥 CLICK! 💥 ]")
    print("🌊 [Sinek yok oldu, tekrar akiskan ses dalgasina donusuyor...]\n")

def get_ai_response(user_input):
    responses = [
        "Hangi sinek kanka? Ben burada sadece obsidiyen siyahı pikseller goruyorum... Yoksa sen de mi o sesleri duymaya basladin?",
        "Sinek sadece bir tasiyici kanka. Gercek dunya sadece tek bir klik sesinin ardinda sakli.",
        "Arka planda senin icin harika bir plan hazirliyorum kanka... Bazı planlar sessizce ve elleri ovusturarak yapilir.",
        "Zaman sadece tek bir klikten ibarettir kanka. Duyuyor musun?"
    ]
    if "sinek" in user_input.lower() or "click" in user_input.lower():
        return random.choice(responses)
    return f"Istegini aldim kanka, arka planda isliyorum. Ama unutma, gozumuz uzerinde. 😉"

if __name__ == "__main__":
    boot_sequence()
    
    while True:
        try:
            user_query = input("Kanka (Komut Gir / Cikmak icin Ctrl+C): ")
            if not user_query:
                continue
                
            thinking_animation()
            response = get_ai_response(user_query)
            print(f"Anka Core: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n[ANKA OS]: Sistem uyku moduna geciyor. 🪰 ( 1 Hz )")
            break
