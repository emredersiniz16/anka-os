#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include <string.h>

// --- CORE/ İÇİNDE OLDUĞUN İÇİN YANINDAKİLERİ İSİMLE ÇAĞIR ---
#include "ui_engine.c"
#include "anim_engine.c" 
#include "agent_logic.c" 
#include "input_handler.c"

// --- CORE/ İÇİNDEN ÇIKIP ANA DİZİNE GİTMEK İÇİN ../ KULLAN ---
#include "../touch_engine.c"
#include "../system_monitor.c"
#include "../battery_engine.c"

// ANKA OS: HACKER SİNEK MOTORU (PROFESYONEL DASHBOARD SÜRÜMÜ)
int main() {
    // --- DEBUG LOG SİSTEMİ ---
    // Her türlü çıktı artık debug.log dosyasına yazılır, cihazda göremesen bile 
    // GitHub'da bu dosyayı kontrol ederek nerede hata aldığını anlarsın.
    freopen("debug.log", "w", stdout);
    freopen("debug.log", "w", stderr);

    printf("🔊 [ANKA OS BOOTING... 💥]\n");

    int fb_fd = open("/dev/fb0", O_RDWR);
    if (fb_fd < 0) {
        printf("Hata: Framebuffer'a ulaşılamadı!\n");
        return 1;
    }

    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd); 

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    // Gönder Butonu Koordinatları (Ekranın sağ alt köşesi)
    int btn_w = (int)(150 * scale); 
    int btn_h = (int)(150 * scale); 
    int btn_x = w - btn_w - (int)(50 * scale); 
    int btn_y = h - btn_h - (int)(50 * scale); 

    int current_state = 0; // FLY_IDLE
    update_fly_animation(current_state, w, h, scale);

    if (init_touch() < 0) {
        printf("⚠️ Uyarı: Dokunmatik sensör pasif.\n");
    }

    printf("🎙️ [SİSTEM]: Sesli uyandırma servisi aktif.\n");

    while(1) {
        char gelen_mesaj[256];
        int touch_x = 0, touch_y = 0;
        
        printf("\n💬 [SESSİZ MOD] Mesajınızı yazın: ");
        if (fgets(gelen_mesaj, sizeof(gelen_mesaj), stdin) == NULL) break;
        
        gelen_mesaj[strcspn(gelen_mesaj, "\n")] = 0;
        if(strlen(gelen_mesaj) == 0) continue;

        printf("👆 Mesaj hazır. Butona dokun...\n");
        while(1) {
            if (get_touch_event(&touch_x, &touch_y)) {
                if (is_button_clicked(touch_x, touch_y, btn_x, btn_y, btn_w, btn_h)) {
                    printf("\n🚀 [İLETİLDİ]\n");
                    break;
                }
            }
            usleep(50000); 
        }

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

        ui_render(final_message, current_state);
        
        current_state = 0; // FLY_IDLE
        update_fly_animation(current_state, w, h, scale);
    }
    return 0;
}
