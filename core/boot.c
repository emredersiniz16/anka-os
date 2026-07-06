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
#include "touch_engine.c" 

// ANKA OS: HACKER SİNEK MOTORU (PROFESYONEL DASHBOARD SÜRÜMÜ)
void main() {
    printf("🔊 [ANKA OS BOOTING... 💥]\n");

    int fb_fd = open("/dev/fb0", O_RDWR);
    if (fb_fd < 0) {
        printf("Hata: Framebuffer'a ulaşılamadı!\n");
        return;
    }

    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd); 

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    int current_state = 0; // FLY_IDLE
    update_fly_animation(current_state, w, h, scale);

    if (init_touch() < 0) {
        printf("⚠️ Uyarı: Dokunmatik sensör pasif.\n");
    }

    printf("🎙️ [SİSTEM]: Sesli uyandırma servisi aktif.\n");

    while(1) {
        char gelen_mesaj[256];
        int touch_x = 0, touch_y = 0;
        
        // 1. ADIM: METİN GİRİŞİ
        printf("\n💬 [SESSİZ MOD] Mesajınızı yazın: ");
        if (fgets(gelen_mesaj, sizeof(gelen_mesaj), stdin) == NULL) break;
        
        gelen_mesaj[strcspn(gelen_mesaj, "\n")] = 0;
        if(strlen(gelen_mesaj) == 0) continue;

        // 2. ADIM: GÖNDER BUTONUNA DOKUNMA BEKLENİR
        printf("👆 Mesaj hazır. Butona dokun...\n");
        while(1) {
            if (get_touch_event(&touch_x, &touch_y)) {
                // Burada buton koordinatlarını (btn_x, btn_y) ui_engine içinden alabiliriz 
                // ama sabit değerlerle kontrolü buraya da ekledik
                if (is_button_clicked(touch_x, touch_y, w-(int)(200*scale), h-(int)(200*scale), (int)(150*scale), (int)(150*scale))) {
                    printf("\n🚀 [İLETİLDİ]\n");
                    break;
                }
            }
            usleep(50000); 
        }

        // 3. ADIM: ZEKA VE GÖRSEL GÜNCELLEME
        current_state = 1; // FLY_THINK
        update_fly_animation(current_state, w, h, scale);

        char command[512];
        sprintf(command, "python3 agents/fly_brain.py \"%s\"", gelen_mesaj);
        
        char final_message[1024] = {0};
        FILE *fp = popen(command, "r");
        if (fp != NULL) {
            fgets(final_message, sizeof(final_message), fp);
            pclose(fp);
        }

        // Profesyonel panel güncellenir: Mesaj + Durum (current_state)
        ui_render(final_message, current_state);
        
        current_state = 0; // FLY_IDLE
        update_fly_animation(current_state, w, h, scale);
    }
}
