#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Sinek Görsel Motoru (GERÇEK GIF BAĞLANTISI)
void update_fly_animation(int current_state) {
    
    // Önce ekrandaki eski GIF'i temizle (üst üste binmemesi için)
    system("pkill -f fbi > /dev/null 2>&1");

    if (current_state == 0) {
        // 0 = FLY_IDLE (Bekleme Modu)
        printf("\n🪰 [GÖRSEL AKTİF]: assets/sinek_ucuyor.GIF ekrana yansıtılıyor...\n");
        
        // Framebuffer üzerinden senin Uçan Sinek GIF'ini ekrana basar
        // (Arka planda çalışması için komutun sonuna & koyduk)
        system("fbi -d /dev/fb0 -a -noverbose -T 1 assets/sinek_ucuyor.GIF &"); 
    } 
    else if (current_state == 1) {
        // 1 = FLY_THINK (İşlem / Hack Modu)
        printf("\n⚡ [GÖRSEL AKTİF]: assets/sinek_dusunen.GIF ekrana yansıtılıyor...\n");
        
        // Cihaz düşünürken senin Düşünen Sinek GIF'ini devreye sokar
        system("fbi -d /dev/fb0 -a -noverbose -T 1 assets/sinek_dusunen.GIF &");
    }
}
