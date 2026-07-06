#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include "ui_engine.c"
#include "anim_engine.c" // Animasyon motorunu ekledik

// ANKA OS: ANİMASYONLU SİNEK MOTORU
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
        // Simülasyon: Rastgele bir tetikleyici gelirse (örn: Butona basıldı)
        // Burada gerçek input_handler devreye girecek
        
        // Örnek tetikleyici:
        // current_state = 1; // FLY_THINK
        // update_fly_animation(current_state);

        printf("🪰 Ajan Sinek aktif durumda.\n");
        sleep(1); 
    }
}
