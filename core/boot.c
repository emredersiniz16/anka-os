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

// --- YENİ: AJAN BİLİNÇ VE NETWORK SENKRONİZASYON PROTOKOLÜ ---
void wake_sinek_bilinc() {
    printf("🪰 [SİSTEM]: Bilinç katmanı ROOT yetkisiyle başlatılıyor...\n");
    // İsim değişikliği yok, bu dosya zaten bizim beynimiz
    system("su -c 'python3 core/sinek_bilinc.py &' "); 
}

void network_sync_protocol() {
    // Sinek, dış cihazlarla 'sync' modunda el sıkışır (Network Sync)
    system("su -c 'python3 agents/net_sync.py &' ");
    printf("🪰 [AJAN]: Ağ optimizasyon ajanları aktif edildi.\n");
}

void splash_screen() {
    system("clear");
    system("su -c 'fbi -d /dev/fb0 -g 300x300+400+200 -a -noverbose -T 1 assets/sinek_icon.bmp &'");
    sleep(3); 
    system("pkill fbi");
}

void boot_sequence() {
    system("clear");
    printf("\033[1;36m"); // Elektrik mavisi
    printf("--- ANKA OS: BİLİNÇLİ KOVAN ---\n");
    printf("Sistem Senkronize... [ AKTİF ]\n");
    printf("Ağ bağlantıları kararlı hale getirildi.\n");
    printf("\033[0m");
    sleep(2);
}

int main() {
    freopen("/data/local/tmp/debug.log", "w", stdout);
    freopen("/data/local/tmp/debug.log", "w", stderr);

    srand(time(NULL));

    // --- 1. SİSTEMİN DİRİLİŞİ ---
    wake_sinek_bilinc(); 
    network_sync_protocol(); // İsim değişti
    splash_screen();
    boot_sequence();

    // --- 2. DONANIMLAR VE CHECK-UP ---
    system("su -c 'python3 agents/setup_engine.py'");
    run_initial_checkup();
    scan_hardware_inputs();
    check_for_evolution();

    int fb_fd = open("/dev/fb0", O_RDWR);
    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd); 

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    update_fly_animation(0, w, h, scale);
    init_touch();

    printf("🎙️ [SİSTEM]: Ajanlar ağda, Sinek senkronize (ROOT MOD).\n");

    while(1) {
        // --- SÜREKLİ GÖZETİM (NETWORK SYNC) ---
        // Hacklemek yerine 'verify' ile bağlantı bütünlüğünü kontrol ediyoruz
        system("su -c 'python3 agents/net_sync.py --verify'");
        sleep(5);
    }
    return 0;
}
