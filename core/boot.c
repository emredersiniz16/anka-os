#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include <string.h>

// --- CORE MODÜLLERİ ---
#include "ui_engine.c"
#include "anim_engine.c" 
#include "agent_logic.c" 
#include "input_handler.c"
#include "audio_engine.c" 

// --- ANA DİZİN MODÜLLERİ ---
#include "../touch_engine.c"
#include "../system_monitor.c"
#include "../battery_engine.c"

int main() {
    freopen("debug.log", "w", stdout);
    freopen("debug.log", "w", stderr);

    // --- İLK KURULUM KONTROLÜ (MASTER SETUP) ---
    // Sistem arayüzü yüklemeden önce ajanımızı çağırıp kurulum yapılıp yapılmadığına bakar.
    system("python3 agents/setup_engine.py");

    printf("🔊 [ANKA OS BOOTING... 💥]\n");

    int fb_fd = open("/dev/fb0", O_RDWR);
    if (fb_fd < 0) return 1;
    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd); 

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    int btn_w = (int)(150 * scale); 
    int btn_h = (int)(150 * scale); 
    int btn_x = w - btn_w - (int)(50 * scale); 
    int btn_y = h - btn_h - (int)(50 * scale); 

    int current_state = 0; 
    update_fly_animation(current_state, w, h, scale);
    init_touch();

    printf("🎙️ [SİSTEM]: Sesli uyandırma ve hacker modülleri aktif.\n");

    while(1) {
        // --- 1. AŞAMA: SESLİ UYANDIRMA (HEY SİNEK) ---
        record_audio(3); 
        if (check_wake_word("/tmp/anka_voice.wav")) {
            // İleride bu kısmı profile.json'dan okuyarak dinamik hale getirebiliriz!
            speak("Efendim, seni dinliyorum."); 
        } else {
            continue; 
        }

        // --- 2. AŞAMA: KOMUT İŞLEME ---
        char gelen_mesaj[256];
        printf("\n💬 [SESSİZ MOD] Mesajınızı yazın: ");
        if (fgets(gelen_mesaj, sizeof(gelen_mesaj), stdin) == NULL) break;
        gelen_mesaj[strcspn(gelen_mesaj, "\n")] = 0;
        if(strlen(gelen_mesaj) == 0) continue;

        current_state = 1; // FLY_THINK
        update_fly_animation(current_state, w, h, scale);

        // Bulut beynini tetikle
        char command[512];
        sprintf(command, "python3 agents/fly_brain.py \"%s\"", gelen_mesaj);
        
        char final_message[1024] = {0};
        FILE *fp = popen(command, "r");
        if (fp != NULL) {
            fgets(final_message, sizeof(final_message), fp);
            pclose(fp);
        }

        // --- 3. AŞAMA: YANITI SESLENDİR ---
        ui_render(final_message, current_state);
        speak(final_message); // Buluttan gelen zeka cevabını sesli oku!
        
        current_state = 0; // FLY_IDLE
        update_fly_animation(current_state, w, h, scale);
    }
    return 0;
}
