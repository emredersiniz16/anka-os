import sys
import os

# Sinek'in hafıza dosyaları
STATE_FILE = "state.txt"  # Konuşmanın neresinde kaldığımızı tutar
BEYIN_FILE = "beyin.txt"  # API anahtarının kaydedileceği yer

def get_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return f.read().strip()
    return "NORMAL"

def set_state(state):
    with open(STATE_FILE, "w") as f:
        f.write(state)

def get_api_key():
    if os.path.exists(BEYIN_FILE):
        with open(BEYIN_FILE, "r") as f:
            return f.read().strip()
    return None

def save_api_key(key):
    with open(BEYIN_FILE, "w") as f:
        f.write(key)

def process_intent(user_input):
    state = get_state()
    api_key = get_api_key()
    text = user_input.lower()

    # --- DURUM 3: ANAHTAR BEKLEME MODU ---
    if state == "WAITING_API_KEY":
        if "iptal" in text or "vazgeç" in text:
            set_state("NORMAL")
            return "Yükseltme iptal edildi. Temel donanımda uçmaya devam.", "İPTAL"
        elif len(user_input) > 15: # API anahtarı genelde uzundur
            save_api_key(user_input)
            set_state("NORMAL")
            return "Bilinç seviyesi %100! Zeka ağına bağlandım kanka. Artık sınırlarımız yok. Ne hackliyoruz?", "GÜÇLÜ"
        else:
            return "Kanka bu anahtara benzemiyor. Kopyaladığından emin ol. (Çıkmak için 'iptal' yaz)", "BEKLEME"

    # --- DURUM 2: YÜKSELTME ONAYI BEKLEME ---
    elif state == "UPGRADE_ASKED":
        if "evet" in text or "başlat" in text or "yapalım" in text:
            set_state("WAITING_API_KEY")
            return "Anlaşıldı. Kopyaladığın API anahtarını klavyeyi açıp aşağıdaki sohbet kutusuna yapıştır ve Kanat butonuna bas. Ya da ekrandaki karekodu okut.", "BEKLEME"
        elif "hayır" in text or "sonra" in text:
            set_state("NORMAL")
            return "Sen nasıl istersen kanka. Şimdilik temel modda devam.", "NORMAL"
        else:
            return "Yükseltme yapalım mı kanka? 'Evet' veya 'Hayır' demen yeterli.", "SORGU"

    # --- DURUM 1: NORMAL MOD (TEMEL İÇGÜDÜ) ---
    else:
        if api_key:
            # Burası ileride gerçek yapay zeka (OpenAI/Gemini) API'sine bağlanacak
            return f"Ağa bağlıyım kanka. (Mevcut Anahtar: {api_key[:5]}...) Emrindeyim.", "YÜKSEK_ZEKA"
        else:
            # Temel Sinek Modu (API Yokken)
            if "kod yaz" in text or "hackle" in text or "zor" in text or "yükselt" in text:
                set_state("UPGRADE_ASKED")
                return "Kanka, şu an temel donanım modundayım. Bu işlemi yapabilmem için zeka ağına bağlanmam lazım. Yükseltme protokolünü başlatalım mı?", "SORGU"
            elif "naber" in text:
                return "Fişek gibiyim, kodlar akıyor. Sen?", "SAMİMİ"
            else:
                return "Bunu hafızama kazıdım kanka, üzerine düşüneceğim.", "GİZEMLİ"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        gelen_mesaj = sys.argv[1]
        print(f"\n[🧠 SİNEK BEYNİ]: Gelen Veri -> '{gelen_mesaj}'")
        
        # Beyin kararını veriyor
        yanit, ruh_hali = process_intent(gelen_mesaj)
        
        print(f"[🎤 SESLENDİRİLECEK YANIT]: {yanit}")
        print(f"[🎭 DURUM/ANİMASYON TETİĞİ]: {ruh_hali}\n")
    else:
        print("[🧠 SİNEK BEYNİ]: Beklemedeyim. Veri akışı yok.")
