import json
import urllib.request
import urllib.error

# NOT: Bu kod cihaza inmez, doğrudan RAM üzerinde çalışır!
# fly_brain.py tarafından buraya GELEN_MESAJ ve API_ANAHTARI değişkenleri aktarılır.

def bulut_zekasina_sor(mesaj, anahtar):
    # Eğer API anahtarı henüz girilmediyse veya test aşamasındaysak:
    if len(anahtar) < 15 or anahtar == "KULLANICI_API_ANAHTARI_BURADA_OLACAK":
        return f"☁️ BULUTTAN CEVAP: Kanka bağlantı başarılı! Sıfır depolama sistemi RAM üzerinde tıkır tıkır çalışıyor. Gelen mesajın: '{mesaj}'"

    # OpenAI / Groq / OpenRouter gibi bir sağlayıcının standart API yapısı
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {anahtar}"
    }
    
    # Anka OS'a bir karakter (Persona) yüklüyoruz
    sistem_mesaji = "Sen Anka OS'un siberpunk asistanısın. Kısa, net, hacker tarzı ve samimi ('kanka' diyerek) cevaplar ver."
    
    data = {
        "model": "gpt-3.5-turbo", # İleride bunu en ucuz/en hızlı modelle değiştirebiliriz
        "messages": [
            {"role": "system", "content": sistem_mesaji},
            {"role": "user", "content": mesaj}
        ],
        "max_tokens": 150
    }
    
    try:
        # İnternet üzerinden API'ye vuruyoruz (Ekstra kütüphane kullanmadan, saf Python ile)
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            res_json = json.loads(res_body)
            # Yapay zekanın verdiği cevabı döndür
            return res_json['choices'][0]['message']['content']
            
    except Exception as e:
        return f"Zeka ağına vururken şalter attı kanka: {e}"

# Kod RAM'e çekildiği an burası otomatik tetiklenir
try:
    nihai_cevap = bulut_zekasina_sor(GELEN_MESAJ, API_ANAHTARI)
    print(nihai_cevap) # C çekirdeği (boot.c) bu çıktıyı alıp ekrana (Sinek motoruna) basacak!
except Exception as e:
    print("Bulut motoru çalışırken bir hata oluştu.")
