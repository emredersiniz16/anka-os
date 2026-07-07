#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include <string.h>
#include <time.h>

// --- CORE MODÜLLERİ ---
#include "ui_engine.c"
#include "anim_engine.c" 
#include "agent_logic.c" 
#include "input_handler.c"
#include "audio_engine.c" 
#include "camera_engine.c"  
#include "gallery_engine.c" 
#include "idle_engine.c"    
#include "checkup.c"        
#include "input_engine.c"    // YENİ: Dinamik Tuş Dedektifi
#include "ota_engine.c"      // YENİ: Evrim Motoru

// --- ANA DİZİN MODÜLLERİ ---
#include "../touch_engine.c"
#include "../system_monitor.c"
#include "../battery_engine.c"

int main() {
    freopen("debug.log", "w", stdout);
    freopen("debug.log", "w", stderr);

    srand(time(NULL));

    // --- 1. İLK KURULUM VE CHECK-UP ---
    system("python3 agents/setup_engine.py");
    printf("🔊 [ANKA OS BOOTING... 💥]\n");

    // Donanım dedektifini çalıştır
    run_initial_checkup();
    
    // YENİ: Donanım yeteneklerini (tuş/dokunmatik) tanı
    scan_hardware_inputs();
    
    // YENİ: Bulutta güncelleme var mı bak ve donanıma göre onayı iste
    check_for_evolution();

    int fb_fd = open("/dev/fb0", O_RDWR);
    if (fb_fd < 0) return 1;
    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd); 

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    int current_state = 0; 
    update_fly_animation(current_state, w, h, scale);
    init_touch();

    printf("🎙️ [SİSTEM]: Tüm Siberpunk Modüller ve Sensörler Aktif.\n");

    while(1) {
        // --- 1. AŞAMA: SESLİ UYANDIRMA VE PUSU MODU ---
        record_audio(3); 
        if (check_wake_word("/tmp/anka_voice.wav")) {
            speak("Efendim, seni dinliyorum."); 
        } else {
            run_idle_orchestrator(w, h);
            continue; 
        }

        // --- 2. AŞAMA: KOMUT İŞLEME ---
        char gelen_mesaj[256];
        printf("\n💬 [SESSİZ MOD] Mesajınızı yazın: ");
        if (fgets(gelen_mesaj, sizeof(gelen_mesaj), stdin) == NULL) break;
        gelen_mesaj[strcspn(gelen_mesaj, "\n")] = 0;
        if(strlen(gelen_mesaj) == 0) continue;

        // === CANLI YAYIN (KAMERA AÇ/KAPAT) ===
        if (strstr(gelen_mesaj, "kamerayı aç") != NULL || strstr(gelen_mesaj, "canlı yayın") != NULL) {
            speak("Gözlerimi açıyorum kanka. Kapatmak istersen 'kamerayı kapat' demen yeterli.");
            open_live_camera();
            continue; 
        }
        else if (strstr(gelen_mesaj, "kamerayı kapat") != NULL || strstr(gelen_mesaj, "yayını kapat") != NULL) {
            speak("Gözleri kapattım kanka. Ben buradayım.");
            close_live_camera();
            update_fly_animation(current_state, w, h, scale); 
            continue; 
        }

        // === AKICI GALERİ ===
        else if (strstr(gelen_mesaj, "galeri") != NULL || strstr(gelen_mesaj, "kütüphane") != NULL) {
            speak("Kütüphaneyi açıyorum. Çıkmak için ekranın altına dokun.");
            load_gallery();
            show_current_photo();
            
            int touch_x = 0, touch_y = 0;
            int ilk_dokunus_x = -1;
            
            while(1) {
                if (get_touch_event(&touch_x, &touch_y)) {
                    if (touch_y > h - 200) { 
                        speak("Galeriden çıkılıyor.");
                        break; 
                    }

                    if (ilk_dokunus_x == -1) {
                        ilk_dokunus_x = touch_x; 
                    } else {
                        int swipe_durumu = detect_swipe(ilk_dokunus_x, touch_x, 50); 
                        if (swipe_durumu == 1) { 
                            gallery_prev(); 
                            ilk_dokunus_x = -1; 
                            usleep(300000); 
                        } else if (swipe_durumu == 2) { 
                            gallery_next(); 
                            ilk_dokunus_x = -1;
                            usleep(300000);
                        }
                    }
                } else {
                    ilk_dokunus_x = -1; 
                }
                usleep(50000);
            }
            system("clear");
            update_fly_animation(current_state, w, h, scale);
            continue; 
        }

        // === VISION AI (GÖZÜN ANLIK ANALİZİ) ===
        if (strstr(gelen_mesaj, "şuna bak") != NULL || strstr(gelen_mesaj, "fotoğraf") != NULL ||
            strstr(gelen_mesaj, "bu ne") != NULL || strstr(gelen_mesaj, "çöz") != NULL ||
            strstr(gelen_mesaj, "hesapla") != NULL || strstr(gelen_mesaj, "bitki") != NULL) {
            
            trigger_vision_process(); 
            capture_image(); 
            speak("Gözüm üstünde kanka. İnceliyorum, biraz bekle...");
        }

        // --- 3. AŞAMA: BULUT ZEKASI (FLY BRAIN) ---
        current_state = 1; 
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
        
        current_state = 0; 
        update_fly_animation(current_state, w, h, scale);
    }
    return 0;
}
