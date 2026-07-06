#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include "ui_engine.c"
#include "anim_engine.c" 
#include "agent_logic.c" // 🧠 Zeka motorunu buraya bağladık

// ANKA OS: ANİMASYONLU VE ZEKİ SİNEK MOTORU
void main() {
    printf("🔊 [💥 CLICK! 💥]\n");

    // Donanım Erişim
    int fb_fd = open("/dev/fb0", O_RDWR);
    if (fb_fd < 0) {
        printf("Hata: Framebuffer'a ulaşılamadı!\n");
        return;
    }

    // Başlangıç: Sinek uçuyor
    int current_state = 0; // 0 = FLY_IDLE
    update_fly_animation(current_state);

    while(1) {
        // --- SİMÜLASYON: Dışarıdan sesli komut geldiğini varsayıyoruz ---
        char gelen_mesaj[] = "sinek bu nasıl çalışıyor";
        
        // 1. Zeka Devrede: Gelen mesajın niyetini çöz (Kanka modu mu, komut mu?)
        analyze_input(gelen_mesaj);
        
        // 2. Animasyon Devrede: Ajan düşünme moduna geçer ve gif değişir
        current_state = 1; // 1 = FLY_THINK
        update_fly_animation(current_state);

        printf("🪰 Ajan Sinek aktif durumda.\n");
        
        // Döngü saniyede bir ekranı boğmasın diye bekleme süresini 5 saniyeye çektim
        sleep(5); 
    }
}
