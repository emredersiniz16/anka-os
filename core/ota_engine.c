// ota_engine.c - EVRİM VE OTA PROTOKOLÜ (FULL ENTEGRE)
#include <stdio.h>
#include <stdlib.h>
#include "hardware_types.h" // Yapı tanımını (struct) içeri dahil ediyoruz

extern DeviceHardware current_hardware;

// Eksik olan fonksiyon prototiplerini buraya ekledik (linker hatasını önler)
int user_confirmed_evolution();

void check_for_evolution() {
    printf("\n=================================================\n");
    printf("        [ SİNEK EVRİM PROTOKOLÜ AKTİF ]        \n");
    printf("=================================================\n");
    
    // 1. GitHub bağlantısını kontrol et
    printf("SİNEK: Kovan zihni bulutla senkronize ediliyor...\n");
    int status = system("git -C /data/local/tmp/anka-os fetch origin main");
    
    if (status == 0) {
        printf("SİNEK: Kanka bulutta yeni hücreler inşa etmişsin, zekamı güncelleyeyim mi?\n\n");
        
        // 2. Donanıma göre kullanıcıdan onay al
        if (current_hardware.has_home_button) {
            printf("👉 Onaylamak icin o meshur ORTA TUSA bas.\n");
        } else if (current_hardware.has_touch_screen) {
            printf("👉 Zekami guncellemek icin ekrani YUKARI KAYDIR.\n");
        } else {
            printf("👉 Guncelleme icin SES ACMA tusuna bas.\n");
        }
        
        // 3. Kullanıcı onayını bekle ve EvrimMotoru'nu tetikle
        if (user_confirmed_evolution()) { 
            printf("👉 [OTA]: Evrim başlatılıyor... Kovan yeniden yapılandırılıyor.\n");
            system("su -c 'python3 core/evrim_motoru.py --payload universal_sinek.bin &'");
        } else {
            printf("👉 [OTA]: Evrim ertelendi. Mevcut bilinç korunuyor.\n");
        }
    } else {
        printf("SİNEK: Kovan stabil, güncelleme gerekmiyor.\n");
    }
    
    printf("=================================================\n");
}
