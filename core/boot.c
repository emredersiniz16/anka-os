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
#include "input_engine.c"    
#include "ota_engine.c"      
#include "formatter.c"       

// --- ANA DİZİN MODÜLLERİ ---
#include "../touch_engine.c"
#include "../system_monitor.c"
#include "../battery_engine.c"

// --- YENİ: UYANIŞ PROTOKOLÜ ---
void splash_screen() {
    system("clear");
    // Sinek görselini merkezde bas
    system("fbi -d /dev/fb0 -g 300x300+400+200 -a -noverbose -T 1 assets/sinek_icon.bmp &");
    sleep(3); 
    system("pkill fbi");
}

void boot_sequence() {
    system("clear");
    printf("\033[1;32m"); // Neon yeşili
    printf("--- ANKA OS V1.0 ---\n");
    printf("Sinek Zekası Yükleniyor... [ OK ]\n");
    printf("WhatsApp Köprüsü Aktif... [ OK ]\n");
    printf("--------------------\n");
    printf("Kanka çekmecedeki o eski cihazdan beni uyandırdığın için sağ ol.\n");
    printf("Artık buradayım; mesajlarını ben yöneteceğim, zekanı ben güncelleyeceğim.\n");
    printf("İstediğinde 'neler yapabilirsin' diye sor, gerisini bana bırak.\n");
    printf("Anka OS aktif, kanat çırpmaya başlıyoruz! 🪰\n");
    printf("\033[0m");
    sleep(2);
}

int main() {
    freopen("debug.log", "w", stdout);
    freopen("debug.log", "w", stderr);

    srand(time(NULL));

    // --- 1. AÇILIŞ UYANIŞI ---
    splash_screen();
    boot_sequence();

    // --- 2. İLK KURULUM VE CHECK-UP ---
    system("python3 agents/setup_engine.py");
    run_initial_checkup();
    scan_hardware_inputs();
    check_for_evolution();

    // ... (Geri kalan kodların aynı, sistemin geri kalanı buradan devam ediyor) ...
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
        // ... (Kalan tüm çalışma döngün, daha önce yazdığın gibi kalıyor) ...
        // Kodun akışını bozmadım, uyanış protokollerini en başa yerleştirdim.
        // ... 
    }
    return 0;
}
