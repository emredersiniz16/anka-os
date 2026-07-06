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
#include "camera_engine.c"  // YENİ: Sinek Gözü (Vision AI)
#include "gallery_engine.c" // YENİ: Akıcı Galeri Motoru

// --- ANA DİZİN MODÜLLERİ ---
#include "../touch_engine.c"
#include "../system_monitor.c"
#include "../battery_engine.c"

int main() {
    freopen("debug.log", "w", stdout);
    freopen("debug.log", "w", stderr);

    // --- İLK KURULUM KONTROLÜ (MASTER SETUP) ---
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

    printf("🎙️ [SİSTEM]: Tüm Siberpunk Modüller ve Sensörler Aktif.\n");

    while(1) {
        // --- 1. AŞAMA: SESLİ UYANDIRMA (HEY SİNEK) ---
        record_audio(3); 
        if (check_wake_word("/tmp/anka_voice.wav")) {
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

        // === VISION AI (GÖZ) TETİKLEYİCİSİ ===
        if (strstr(gelen_mesaj, "şuna bak") != NULL || strstr(gelen_mesaj, "fotoğraf") != NULL) {
            trigger_vision_process(); // Sinek gözlerini açar (Log basar)
            capture_image();          // Görüntüyü çeker ve kütüphaneye atar
            speak("Görüntüyü aldım kanka. Kütüphaneye ekledim ve inceliyorum.");
        }
        
        // === AKICI GALERİ (FLUID GALLERY) TETİKLEYİCİSİ ===
        else if (strstr(gelen_mesaj, "galeri") != NULL || strstr(gelen_mesaj, "kütüphane") != NULL) {
            speak("Kütüphaneyi açıyorum. Çıkmak için ekranın en altına dokun.");
            load_gallery();
            show_current_photo();
            
            // --- Akıllı Jest (Smart Swipe) Döngüsü ---
            int touch_x = 0, touch_y = 0;
            int ilk_dokunus_x = -1;
            
            while(1) {
                if (get_touch_event(&touch_x, &touch_y)) {
                    // Ekranda en aşağıya dokunursa galeriden çık
                    if (touch_y > h - 200) {
                        speak("Galeriden çıkılıyor.");
                        break; 
                    }

                    if (ilk_dokunus_x == -1) {
                        ilk_dokunus_x = touch_x; // İlk dokunma noktasını al
                    } else {
                        // Parmağın kayma yönünü hesapla
                        int swipe_durumu = detect_swipe(ilk_dokunus_x, touch_x, 50); 
                        if (swipe_durumu == 1) { 
                            gallery_prev(); // Sağa kaydırma (Önceki)
                            ilk_dokunus_x = -1; 
                            usleep(300000); // Peş peşe atlamaması için ufak gecikme
                        } else if (swipe_durumu == 2) { 
                            gallery_next(); // Sola kaydırma (Sonraki)
                            ilk_dokunus_x = -1;
                            usleep(300000);
                        }
                    }
                } else {
                    ilk_dokunus_x = -1; // Parmak çekilince sıfırla
                }
                usleep(50000);
            }
            system("clear");
            update_fly_animation(current_state, w, h, scale);
            continue; // Galeri bitince ana menüye dön
        }

        // --- 3. AŞAMA: BULUT ZEKASI (FLY BRAIN) ---
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

        // --- 4. AŞAMA: YANITI SESLENDİR ---
        ui_render(final_message, current_state);
        speak(final_message); 
        
        current_state = 0; // FLY_IDLE
        update_fly_animation(current_state, w, h, scale);
    }
    return 0;
}
