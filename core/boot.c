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

// ANKA OS: HACKER SİNEK MOTORU (FINAL ETKİLEŞİM)
void main() {
    printf("🔊 [ANKA OS BOOTING... 💥]\n");

    int fb_fd = open("/dev/fb0", O_RDWR);
    if (fb_fd < 0) {
        printf("Hata: Framebuffer'a ulaşılamadı!\n");
        return;
    }

    int current_state = 0; // FLY_IDLE
    update_fly_animation(current_state);

    while(1) {
        char gelen_mesaj[256];
        
        // --- KANAT BUTONU VE KLAVYE DİNLEME HATTI ---
        // Sistem burada durur ve senden metin girmeni bekler
        printf("\n[KANAT BUTONU] Emret kanka: ");
        if (fgets(gelen_mesaj, sizeof(gelen_mesaj), stdin) == NULL) {
            break;
        }
        
        // Enter'a basıldığında oluşan alt satır karakterini temizle
        gelen_mesaj[strcspn(gelen_mesaj, "\n")] = 0;
        
        // Eğer hiçbir şey yazmadan Kanat'a basarsan başa dön, sistemi yorma
        if(strlen(gelen_mesaj) == 0) continue;

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

        // 1. Zeka Devrede: Sinek'in cevabını gece/gündüz temalı UI penceresine gönder
        ui_render(final_message);
        
        // 2. Animasyon Devrede: Düşünme moduna geç
        current_state = 1; 
        update_fly_animation(current_state);
    }
}
