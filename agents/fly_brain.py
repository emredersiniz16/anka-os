import sys
import os
import subprocess
import urllib.request

# --- SİNEK İMZASI ---
FLY_SIGNATURE = "\n\n[FLY_SIGNATURE_ICON]"

# ... (get_state, set_state, get_api_key, save_api_key, check_internet, scan_wifi fonksiyonları aynı kalıyor) ...

# --- SIFIR DEPOLAMA (ZERO-STORAGE) BULUT KÖPRÜSÜ ---
def buluttan_cek_ve_calistir(ajan_url, kullanici_mesaji, api_anahtari):
    try:
        req = urllib.request.Request(ajan_url)
        with urllib.request.urlopen(req) as response:
            ajan_kodu = response.read().decode('utf-8')
        
        calisma_alani = {
            'GELEN_MESAJ': kullanici_mesaji,
            'API_ANAHTARI': api_anahtari
        }
        
        # Bulut zekasını çalıştır
        exec(ajan_kodu, calisma_alani)
        
        # --- DÜZELTME: İmzayı SADECE bulut cevabı dönerken ekliyoruz ---
        # Ajan kodu kendi çıktısını print ile basıyor, 
        # buraya bir "imza_bas()" fonksiyonu veya etiketi ekliyoruz:
        print(FLY_SIGNATURE) 
        
        return True
    except Exception as e:
        return False

def process_intent(user_input):
    state = get_state()
    api_key = get_api_key()
    text = user_input.lower()

    # --- 1. YEREL KOMUTLAR (İMZA YOK) ---
    if not check_internet():
        if "karekod" in text: return trigger_qr_scan()
        elif "wps" in text: return trigger_wps_connection()
        # ... (diğer yerel komutlar)

    # --- 2. DURUM YÖNETİMİ (İMZA YOK) ---
    # ... (state kontrolleri aynı)

    # --- 4. BULUT ZEKASI (BURADA İMZA VAR) ---
    hedef_bulut_kodu = "https://raw.githubusercontent.com/emredersiniz16/anka-os/main/agents/core_logic.py"
    basarili = buluttan_cek_ve_calistir(hedef_bulut_kodu, user_input, api_key)
    
    if basarili:
        sys.exit(0)
    else:
        return "Bulut zekasına ulaşılamadı. Sunucu hatası kanka." 
