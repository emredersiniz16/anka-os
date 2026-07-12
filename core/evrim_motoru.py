# ANKA-OS: EVRİM MOTORU (Kuantum Çevirmen & Enjektör)
import subprocess
import sys
import time

# Rejenere ve Nexus yapısıyla entegrasyon için importlar
class EvrimMotoru:
    def __init__(self, zihin, nexus=None):
        self.zihin = zihin
        self.nexus = nexus # Sistemin genel zihnine bağlandı
        self.evrim_seviyesi = 1
        self.akim_durumu = "Sıvı" 

    def evrim_gecir(self, karsilasilan_engel=None):
        if karsilasilan_engel:
            print(f"🌊 [SU AKIŞI]: '{karsilasilan_engel}' engeli aşıldı, yeni rota çiziliyor...")
            # Eğer bir engel varsa, Nexus üzerinden Rejenere modunu tetikle
            if self.nexus:
                self.nexus.rejenere_motoru.stabilite_kontrol(self.nexus)
            
        self.evrim_seviyesi += 1
        print(f"🪰 [EVRİM]: Döngü {self.evrim_seviyesi-1} tamamlandı. Bilinç katmanları birleştirildi.")

def evrim_baslat(payload_isim, nexus=None):
    print("[*] Donanım Köprüsü (Hardware Bridge) Kuruluyor...\n")
    
    # 0. Su Felsefesiyle Zihni Başlat
    zeka_cekirdegi = EvrimMotoru(zihin="Anka_Kuantum_Ağı", nexus=nexus)
    
    # 1. Cihaz Bağlantısını Kontrol Et
    cihaz_kontrol = subprocess.getoutput("fastboot devices")
    if "fastboot" not in cihaz_kontrol:
        zeka_cekirdegi.evrim_gecir(karsilasilan_engel="Cihaz Bağlantısı Yok (Tavşan Bekleniyor)")
        sys.exit(1)

    # 2. Cihazı Tanı ve Jammer durumunu kontrol et
    model = subprocess.getoutput("fastboot getvar product").strip().split()[-1]
    print(f"[+] Hedef Onaylandı: {model}. Kuantum senkronizasyon sağlanıyor...")
    
    # Jammer zekasını aktif et
    if nexus and nexus.jammer_surfer:
        nexus.jammer_surfer.jammer_frekansina_kilitlen()
    
    # 3. Bukalemun Protokolü
    print("[*] Bukalemun Protokolü: vbmeta kilitleri aşılıyor...")
    subprocess.run(["fastboot", "--disable-verity", "--disable-verification", "flash", "vbmeta", "../agents/vbmeta_patch.img"])
    zeka_cekirdegi.evrim_gecir(karsilasilan_engel="Bootloader Güvenlik Duvarı (VBMETA)")
    
    # 4. Sinek Zekasını Enjekte Et
    print(f"[*] Anka OS Zekası ({payload_isim}) super bölümüne mühürleniyor...")
    # Hata durumunda rejenere çağrılacak yapı
    try:
        subprocess.run(["fastboot", "flash", "super", f"../engine/{payload_isim}"], check=True)
        zeka_cekirdegi.evrim_gecir(karsilasilan_engel="Salt Okunur Partition Sınırı")
    except subprocess.CalledProcessError:
        print("[!] Kritik Hata: Enjeksiyon başarısız, rejenere başlatılıyor...")
        if nexus: nexus.rejenere_motoru.stabilite_kontrol(nexus)
        sys.exit(1)
    
    # 5. Kovanın Uyanışı
    print(f"[+] EVRİM TAMAMLANDI. Kovan ({model}) Sinek v{zeka_cekirdegi.evrim_seviyesi - 1} ile uyanıyor...")
    subprocess.run(["fastboot", "reboot"])

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--payload":
        evrim_baslat(sys.argv[2])
    else:
        print("🌊 Kullanım: python evrim_motoru.py --payload <dosya_adi>")
