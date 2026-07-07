#include <stdio.h>

extern DeviceHardware current_hardware;

void check_for_evolution() {
    printf("\n=================================================\n");
    printf("        [ SİNEK EVRİM PROTOKOLÜ AKTİF ]        \n");
    printf("=================================================\n");
    
    // İnternetten GitHub version.txt kontrolü yapıldığını varsayıyoruz
    printf("SİNEK: Kanka bulutta yeni hücreler inşa etmişsin, zekamı güncelleyeyim mi?\n\n");
    
    // Donanıma göre dinamik mesaj!
    if (current_hardware.has_home_button) {
        printf("👉 Onaylamak icin o meshur ORTA TUSA bas.\n");
        printf("👉 İptal icin GERI tusuna dokun.\n");
    } 
    else if (current_hardware.has_touch_screen) {
        printf("👉 Zekami guncellemek icin ekrani YUKARI KAYDIR.\n");
        printf("👉 İptal icin ASAGI KAYDIR.\n");
    } 
    else {
        printf("👉 Guncelleme icin SES ACMA, Iptal icin SES KISMA tusuna bas.\n");
    }
    
    printf("=================================================\n");
    
    // Burada sistem kullanıcının tuş/kaydırma hareketini dinlemeye başlar
}
