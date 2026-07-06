#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include <string.h>
#include "ui_engine.c"
#include "anim_engine.c" 
#include "agent_logic.c" 

// ANKA OS: HACKER SİNEK MOTORU
void main() {
    printf("🔊 [ANKA OS BOOTING... 💥]\n");

    int fb_fd = open("/dev/fb0", O_RDWR);
    if (fb_fd < 0) {
        printf("Hata: Framebuffer'a ulaşılamadı!\n");
        return;
    }

    int current_state = 0; // 0 = FLY_IDLE
    update_fly_animation(current_state);

    while(1) {
        // Kullanıcıdan gelen metin (Burası UI'dan gelecek metin değişkeni olacak)
        char gelen_mesaj[] = "yükselt"; 
        
        printf("🪰 Beyin tetikleniyor: '%s'\n", gelen_mesaj);

        // 1. Zeka Devrede: C içinden Python Ajan Beynini çağır
        // Bu komut Python'a gidiyor, kararı alıyor ve sonucu ekrana döküyor
        char command[512];
        sprintf(command, "python3 agents/fly_brain.py \"%s\"", gelen_mesaj);
        system(command);
        
        // 2. Animasyon Devrede: Düşünme modunu tetikle
        current_state = 1; // FLY_THINK
        update_fly_animation(current_state);

        printf("🪰 Ajan Sinek zeka ağında karar veriyor.\n");
        
        sleep(5); 
    }
}
