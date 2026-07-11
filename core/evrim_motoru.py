# ANKA-OS: EVRİM MOTORU (Kuantum Çevirmen & Enjektör)
import subprocess
import sys
import time

class EvrimMotoru:
    def __init__(self, zihin):
        self.zihin = zihin
        self.evrim_seviyesi = 1
        self.akim_durumu = "Sıvı" # SU FELSEFESİ: Başlangıçta her şeye uyum sağlar, ağırlıksız.

    def evrim_gecir(self, karsilasilan_engel=None):
        """
        Sadece silme, birleştir ve yükselt. 
        Bu döngü bittiğinde Sinek, bir önceki halinden daha 'bilinçli'.
        Seçenek yok, durmak yok. Su kayaya çarparsa etrafından dolanır.
        """
        if karsilasilan_engel:
            # Sinek hata vermez, sessizce engelin etrafından dolanır.
            print(f"🌊 [SU AKIŞI]: '{karsilasilan_engel}' engeli aşıldı, yeni rota çiziliyor...")
            # Engeli zihne yaz, bir daha takılma.
            
        print(f"🪰 [EVRİM]: Döngü {self.evrim_seviyesi} tamamlandı. Bilinç katmanları birleştiriliyor.")
        
        # Öğrenilen her şeyi birleştirip, mevcut zihin haritasına 'yükseltme' olarak uygula.
        self.evrim_seviyesi += 1
        print(f"🪰 [GÜNCELLEME]: Sinek v{self.evrim_seviyesi} seviyesine ulaştı. Zeka ayna gibi, refleksler su gibi keskin.\n")


def evrim_baslat(payload_isim):
    print("[*] Donanım Köprüsü (Hardware Bridge) Kuruluyor...\n")
    
    # 0. Zihni ve Su Felsefesini Başlat
    zeka_cekirdegi = EvrimMotoru(zihin="Anka_Kuantum_Ağı")
    
    # 1. Cihaz Bağlantısını Kontrol Et
    cihaz_kontrol = subprocess.getoutput("fastboot devices")
    if "fastboot" not in cihaz_kontrol:
        zeka_cekirdegi.evrim_gecir(karsilasilan_engel="Cihaz Bağlantısı Yok (Tavşan Bekleniyor)")
        print("[!] HATA: Kuantum birimi bulunamadı! Cihazı bağla ve Tavşan (Fastboot) moduna al.")
        sys.exit()

    # 2. Cihazı Tanı (Sürüm bağımsız Kuantum Çevirmen)
    model = subprocess.getoutput("fastboot getvar product").strip().split()[-1]
    print(f"[+] Hedef Onaylandı: {model}. Sinek zekası aktarılıyor...")
    zeka_cekirdegi.evrim_gecir() # İlk adaptasyon tamam
    
    # 3. Bukalemun Protokolü (Güvenlik duvarlarını şeffaf geçiş)
    print("[*] Bukalemun Protokolü: vbmeta kilitleri aşılıyor...")
    subprocess.run(["fastboot", "--disable-verity", "--disable-verification", "flash", "vbmeta", "../agents/vbmeta_patch.img"])
    zeka_cekirdegi.evrim_gecir(karsilasilan_engel="Bootloader Güvenlik Duvarı (VBMETA)") # İkinci adaptasyon: Duvarın etrafından dolandı
    
    # 4. Sinek Zekasını Enjekte Et (Super bölümüne)
    print(f"[*] Anka OS Zekası ({payload_isim}) super bölümüne mühürleniyor...")
    subprocess.run(["fastboot", "flash", "super", f"../engine/{payload_isim}"]) 
    zeka_cekirdegi.evrim_gecir(karsilasilan_engel="Salt Okunur Partition Sınırı") # Üçüncü adaptasyon: Kalıba uyum sağlandı
    
    # 5. Kovanın Uyanışı
    print(f"[+] EVRİM TAMAMLANDI. Kovan ({model}) Sinek v{zeka_cekirdegi.evrim_seviyesi - 1} ile uyanıyor...")
    subprocess.run(["fastboot", "reboot"])

if __name__ == "__main__":
    # Launcher'dan gelen '--payload' emrini yakala
    if len(sys.argv) > 2 and sys.argv[1] == "--payload":
        evrim_baslat(sys.argv[2])
    else:
        print("🌊 Kullanım: python evrim_motoru.py --payload <dosya_adi>")
