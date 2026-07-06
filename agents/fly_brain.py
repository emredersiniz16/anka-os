import sys
import os
import subprocess
import urllib.request

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

# --- YEREL AĞ VE HAYATTA KALMA MODÜLLERİ ---
def trigger_qr_scan():
    return "🪰 Kamera aktif, ağ karekodunu göster kanka, şifreyi çözüyorum..."

def trigger_wps_connection():
    subprocess.Popen(["wpa_cli", "wps_pbc"])
    return "🪰 WPS kapısı açık, modeme kilitleniyorum. 120 saniyen var, tuşa bas kanka!"

# --- SIFIR DEPOLAMA (ZERO-STORAGE) BULUT KÖPRÜSÜ ---
def buluttan_cek_ve_calistir(ajan_url, kullanici_mesaji, api_anahtari):
    try:
        req = urllib.request.Request(ajan_url)
        with urllib.request.urlopen(req) as response:
            ajan_kodu = response.read().decode('utf-8')
        
        # Buluttan inen kodun kullanabilmesi için değişkenleri aktarıyoruz
        calisma_alani = {
            'GELEN_MESAJ': kullanici_mesaji,
            'API_ANAHTARI': api_anahtari
        }
        
        # Kodu sadece RAM üzerinde çalıştır (Hafızada yer kaplamaz)
        exec(ajan_kodu, calisma_alani)
        return True
    except Exception as e:
        return False

def process_intent(user_input):
    state = get_state()
    api_key = get_api_key()
    text = user_input.lower()

    # --- 1. ÇEVRİMDİŞİ (İNTERNET YOKSA) YEREL MOD ---
    if not check_internet():
        if "karekod" in text:
            return trigger_qr_scan()
        elif "wps" in text:
            return trigger_wps_connection()
        elif "tara" in text or "ağ" in text:
            aglar = scan_wifi()
            if aglar:
                return f"Radarda şunlar var: {', '.join(aglar)}. Karekod veya WPS ile bağlanalım mı?"
            return "Kanka internet yok, SIM kartı veya modemi kontrol et."

    # --- 2. API ANAHTARI BEKLEME MODU (BYOK) ---
    if state == "WAITING_API_KEY":
        if "iptal" in text:
            set_state("NORMAL")
            return "Yükseltme iptal edildi. Temel moddayım."
        elif len(user_input) > 15:
            save_api_key(user_input)
            set_state("NORMAL")
            return "Bilinç seviyesi %100! Zeka ağına bağlandım kanka."
        return "API anahtarını yapıştır kanka."

    elif state == "UPGRADE_ASKED":
        if "evet" in text:
            set_state("WAITING_API_KEY")
            return "Anahtarı yapıştır ve kanat butonuna bas."
        return "Yükseltme yapalım mı? Evet/Hayır."

    # --- 3. İNTERNET VAR + ANAHTAR YOK (TEMEL MOD) ---
    if not api_key:
        if any(x in text for x in ["kod yaz", "zeka", "yükselt"]):
            set_state("UPGRADE_ASKED")
            return "Temel moddayım. Zeka ağını aktif edelim mi?"
        return "İnternet var ama beyin modülü eksik kanka. Zekamı yükseltmek ister misin?"
    
    # --- 4. İNTERNET VAR + ANAHTAR VAR = BULUT YÜKLEYİCİ AKTİF! ---
    hedef_bulut_kodu = "https://raw.githubusercontent.com/emredersiniz16/anka-os/main/agents/core_logic.py"
    basarili = buluttan_cek_ve_calistir(hedef_bulut_kodu, user_input, api_key)
    
    if basarili:
        # Bulut kodu kendi çıktısını terminale basacağı için buradan sessizce çıkıyoruz
        sys.exit(0)
    else:
        return "Bulut zekasına ulaşılamadı. Sunucu hatası kanka."

if __name__ == "__main__":
    gelen_mesaj = sys.argv[1] if len(sys.argv) > 1 else ""
    yanit = process_intent(gelen_mesaj)
    
    # C çekirdeğinin (boot.c) ekranına temiz yazı basması için sadece mesajı yazdırıyoruz
    if yanit:
        print(yanit)
