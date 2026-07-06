import sys
import time
import requests
import json

# Buraya kendi API anahtarını gireceksin (OpenAI, Gemini vs.)
API_KEY = "SENIN_API_ANAHTARIN_BURAYA_GELECEK"

def ask_real_ai(user_input):
    print("🪰 Sinek: Ağlara bağlanıyorum, bekle...")
    
    # Ajanın "Kişiliğini" (Sistem Promptu) burada belirliyoruz
    system_prompt = """
    Sen 'Anka OS' içinde yaşayan, eski telefonları hayata döndüren zeki ve biraz alaycı bir yapay zeka ajanısın. 
    Kullanıcıya 'Kanka' diye hitap edebilirsin. Cevapların siberpunk tarzında, çok kısa ve net olsun. Asla bir robot gibi konuşma.
    """

    # ÖRNEK: Gerçek bir AI servisine (API) istek atma yapısı
    url = "https://api.ornek-yapay-zeka.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-3.5-turbo", # veya gemini-pro, hangisini seçersek
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 50
    }

    try:
        # API'ye soruyu gönderiyoruz
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()
        
        # Gelen zekice cevabı yakalıyoruz
        ai_cevap = response_data['choices'][0]['message']['content']
        return ai_cevap
    except Exception as e:
        return "Bağlantı koptu kanka, karanlık ağdayım. İnterneti kontrol et."

if __name__ == "__main__":
    # C motorundan (boot.c) gelen mesajı yakalıyoruz
    if len(sys.argv) > 1:
        gelen_mesaj = sys.argv[1]
        print(f"\n[🧠 SİNEK BEYNİ]: Duyulan Ses -> '{gelen_mesaj}'")
        
        # Gerçek yapay zekaya soruyu sor
        gercek_yanit = ask_real_ai(gelen_mesaj)
        
        # Bu çıktılar Ses Sentezleyiciye (TTS) gidecek
        print(f"[🎤 AJAN DİYOR Kİ]: {gercek_yanit}\n")
    else:
        print("[🧠 SİNEK BEYNİ]: Beklemedeyim. Veri akışı yok.")
