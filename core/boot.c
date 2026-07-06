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

// ANKA OS: HACKER SİNEK MOTORU (TAM BİRLEŞİK SÜRÜM)
void main() {
    printf("🔊 [ANKA OS BOOTING... 💥]\n");

    int fb_fd = open("/dev/fb0", O_RDWR);
    if (fb_fd < 0) {
        printf("Hata: Framebuffer'a ulaşılamadı!\n");
        return;
    }

    // Ekran çözünürlük ve ölçeklendirme bilgilerini donanımdan okuyoruz
    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd); // Bilgileri aldığımız için güvenli bir şekilde kapatıyoruz

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    // Başlangıç: Sinek kendi koordinatında uçarak beklemeye başlar
    int current_state = 0; // FLY_IDLE
    update_fly_animation(current_state, w, h, scale);

    while(1) {
        char gelen_mesaj[256];
        
        // --- KANAT BUTONU VE KLAVYE DİNLEME HATTI ---
        printf("\n[KANAT BUTONU] Emret kanka: ");
        if (fgets(gelen_mesaj, sizeof(gelen_mesaj), stdin) == NULL) {
            break;
        }
        
        gelen_mesaj[strcspn(gelen_mesaj, "\n")] = 0;
        if(strlen(gelen_mesaj) == 0) continue;

        // 1. Animasyon Tetiklenir: Komut girildiği an Sinek elini yüzünü ovuşturma moduna geçer
        current_state = 1; // FLY_THINK
        update_fly_animation(current_state, w, h, scale);

        printf("🪰 Beyin tetikleniyor: '%s'\n", gelen_mesaj);

        // Python beynini çağır
        char command[512];
        sprintf(command, "python3 agents/fly_brain.py \"%s\"", gelen_mesaj);
        
        char final_message[1024] = {0};
        FILE *fp = popen(command, "r");
        if (fp != NULL) {
            fgets(final_message, sizeof(final_message), fp);
            pclose(fp);
        }

        // 2. Zeka Devrede: Sinek'in ürettiği cevabı gece/gündüz temalı UI penceresine basıyoruz
        ui_render(final_message);
        
        // 3. İşlem Bitti: Cevap ekrana geldikten sonra Sinek tekrar normal uçuş moduna geri döner
        current_state = 0; // FLY_IDLE
        update_fly_animation(current_state, w, h, scale);
    }
}
