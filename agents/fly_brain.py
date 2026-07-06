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

def scan_wifi():
    try:
        result = subprocess.check_output(["nmcli", "-t", "-f", "SSID", "dev", "wifi"], text=True)
        return list(set([ag.strip() for ag in result.split("\n") if ag.strip()]))[:3]
    except:
        return []

# --- HACKER MODÜLLERİ (FAZ 2) ---
def trigger_qr_scan():
    # Kamera üzerinden QR okuma protokolü
    return "🪰 Kamera aktif, ağ karekodunu göster kanka, şifreyi çözüyorum..."

def trigger_wps_attack():
    # WPS üzerinden ağa sızma protokolü
    subprocess.Popen(["wpa_cli", "wps_pbc"])
    return "🪰 WPS kapısı açık, modeme kilitleniyorum. 120 saniyen var, tuşa bas kanka!"

def process_intent(user_input):
    state = get_state()
    api_key = get_api_key()
    text = user_input.lower()

    # --- HACKER KOMUTLARI (AĞ YOKSA AKTİF) ---
    if not check_internet():
        if "karekod" in text:
            return trigger_qr_scan(), "HACKER_MODU"
        elif "wps" in text:
            return trigger_wps_attack(), "HACKER_MODU"
        elif "tara" in text or "ağ" in text:
            aglar = scan_wifi()
            return f"Radarda şunlar var: {', '.join(aglar)}. Karekod, WPS veya şifre ile sızalım mı?", "RADAR_MODU"

    # --- DURUM 3: ANAHTAR BEKLEME ---
    if state == "WAITING_API_KEY":
        if "iptal" in text:
            set_state("NORMAL")
            return "Yükseltme iptal edildi. Temel moddayım.", "NORMAL"
        elif len(user_input) > 15:
            save_api_key(user_input)
            set_state("NORMAL")
            return "Bilinç seviyesi %100! Zeka ağına bağlandım kanka.", "GÜÇLÜ"
        return "API anahtarını yapıştır kanka.", "BEKLEME"

    # --- DURUM 2: YÜKSELTME ONAYI ---
    elif state == "UPGRADE_ASKED":
        if "evet" in text:
            set_state("WAITING_API_KEY")
            return "Anahtarı yapıştır ve kanat butonuna bas.", "BEKLEME"
        return "Yükseltme yapalım mı? Evet/Hayır.", "SORGU"

    # --- DURUM 1: NORMAL MOD ---
    else:
        if not check_internet():
            return "İnternet yok. 'Tara' diyerek ağları listeleyebilirsin.", "RADAR_MODU"
        
        if not api_key:
            if any(x in text for x in ["kod yaz", "hackle", "yükselt"]):
                set_state("UPGRADE_ASKED")
                return "Temel moddayım. Zeka ağını aktif edelim mi?", "SORGU"
            return "Seni dinliyorum kanka.", "NORMAL"
        
        return "Ağa bağlıyım ve zeka ağım aktif. Emrindeyim kanka.", "YÜKSEK_ZEKA"

if __name__ == "__main__":
    gelen_mesaj = sys.argv[1] if len(sys.argv) > 1 else ""
    yanit, ruh_hali = process_intent(gelen_mesaj)
    print(f"[🎤 SESLENDİRİLECEK YANIT]: {yanit}")
    print(f"[🎭 DURUM]: {ruh_hali}")
