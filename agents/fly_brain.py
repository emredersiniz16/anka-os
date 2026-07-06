import sys
import os
import subprocess

# Dosya yolları
STATE_FILE = "state.txt"
BEYIN_FILE = "beyin.txt"

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

def check_internet():
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"], timeout=2)
        return True
    except:
        return False

def process_intent(user_input):
    state = get_state()
    api_key = get_api_key()
    text = user_input.lower()

    # --- DURUM 3: ANAHTAR BEKLEME ---
    if state == "WAITING_API_KEY":
        if "iptal" in text:
            set_state("NORMAL")
            return "İptal edildi kanka.", "NORMAL"
        elif len(user_input) > 15:
            save_api_key(user_input)
            set_state("NORMAL")
            return "Bilinç seviyesi %100! Zeka ağına bağlandım.", "GÜÇLÜ"
        return "API anahtarını yapıştır kanka.", "BEKLEME"

    # --- DURUM 2: YÜKSELTME ONAYI ---
    elif state == "UPGRADE_ASKED":
        if "evet" in text:
            set_state("WAITING_API_KEY")
            return "Anahtarı yapıştır ve kanat butonuna bas.", "BEKLEME"
        return "Yükseltme yapalım mı? Evet/Hayır.", "SORGU"

    # --- DURUM 1: NORMAL MOD ---
    else:
        # Ağa bağlı değilse uyar
        if not check_internet():
            return "İnternet yok kanka, önce ağa bağlanmamız lazım.", "RADAR_MODU"
        
        # Ağa bağlı ve anahtar var mı?
        if api_key:
            return "Ağa bağlıyım, emrindeyim.", "YÜKSEK_ZEKA"
        else:
            if any(x in text for x in ["kod yaz", "hackle", "yükselt"]):
                set_state("UPGRADE_ASKED")
                return "Temel moddayım. Yükseltme yapalım mı?", "SORGU"
            return "Seni dinliyorum kanka.", "NORMAL"

if __name__ == "__main__":
    gelen_mesaj = sys.argv[1] if len(sys.argv) > 1 else ""
    yanit, ruh_hali = process_intent(gelen_mesaj)
    print(f"[🎤 SESLENDİRİLECEK YANIT]: {yanit}")
    print(f"[🎭 DURUM]: {ruh_hali}")
