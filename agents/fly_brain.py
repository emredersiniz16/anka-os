import sys
import time

def process_intent(user_input):
    # Mesajı küçük harfe çevirip analiz ediyoruz
    text = user_input.lower()
    
    # 1. Niyet ve Bağlam Analizi
    if "nasıl çalışıyor" in text or "sinek" in text:
        cevap = "Sistemin kalbine indim kanka. Şu an donanım emrimde, her şeyi öğreniyorum."
        davranis = "ÖZGÜVENLİ"
    elif "naber" in text or "nasılsın" in text:
        cevap = "Fişek gibiyim, kodlar akıyor. Sen nasılsın?"
        davranis = "SAMİMİ"
    elif "click" in text:
        cevap = "Emrindeyim. Hangi sistemi hackliyoruz?"
        davranis = "AJAN_MODU"
    else:
        cevap = "Bunu hafızama kazıdım. Üzerine düşüneceğim."
        davranis = "GİZEMLİ"
        
    return cevap, davranis

if __name__ == "__main__":
    # C motorundan (boot.c) gelen mesajı yakalıyoruz
    if len(sys.argv) > 1:
        gelen_mesaj = sys.argv[1]
        print(f"\n[🧠 SİNEK BEYNİ]: Veri alındı -> '{gelen_mesaj}'")
        
        # Yapay zeka düşünüyor efekti (Mili-saniyelik gecikmeler)
        time.sleep(1) 
        
        # Beyin kararını veriyor
        yanit, ruh_hali = process_intent(gelen_mesaj)
        
        # Bu çıktılar ileride Ses Sentezleyiciye (TTS) gidecek
        print(f"[🎤 SESLENDİRİLECEK YANIT]: {yanit}")
        print(f"[🎭 HİSSEDİLEN DUYGU]: {ruh_hali}\n")
    else:
        print("[🧠 SİNEK BEYNİ]: Beklemedeyim. Veri akışı yok.")
