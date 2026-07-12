// boot.c - SİNEK UYANIŞ PROTOKOLÜ (FULL ENTEGRE - FINAL)
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include <string.h>
#include <time.h>

// --- CORE MODÜLLERİ (Sistem artık tamamen birbirine bağlı) ---
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

// --- SİSTEMİN DİRİLİŞ KOMUTLARI ---
void start_kovan_zihni() {
    printf("🪰 [SİSTEM]: Kovan zihni (Nexus) uyanıyor...\n");
    // Nexus artık Jammer ve Rejenere motorlarını kendi içinde yönetiyor
    system("su -c 'python3 core/sinek_nexus.py &' "); 
}

void network_sync_protocol() {
    // Sinek, dış dünyayla bağlantısını "verify" modunda başlatıyor
    system("su -c 'python3 agents/net_sync.py --init &' ");
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
    printf("\033[1;36m --- ANKA OS: BİLİNÇLİ KOVAN --- \033[0m\n");
    // Sistem daha açılırken ortam taraması (Jammer check)
    system("su -c 'python3 core/jammer_surfer.py --check-boot-env &'");
    printf("Sistem Senkronize... [ AKTİF ]\n");
    sleep(2);
}

int main() {
    freopen("/data/local/tmp/debug.log", "w", stdout);
    freopen("/data/local/tmp/debug.log", "w", stderr);

    srand(time(NULL));

    // --- 1. SİSTEMİN DİRİLİŞİ ---
    start_kovan_zihni(); 
    network_sync_protocol();
    splash_screen();
    boot_sequence();

    // --- 2. DONANIMLAR VE CHECK-UP ---
    // Eğer kurulum hata verirse otomatik kurtarma (Rejenere) devreye girer
    if(system("su -c 'python3 agents/setup_engine.py'") != 0) {
        system("su -c 'python3 core/rejenere_motoru.py --force-recover &'");
    }
    
    run_initial_checkup();
    scan_hardware_inputs();
    check_for_evolution();

    // Ekran ve Dokunmatik yapılandırması
    int fb_fd = open("/dev/fb0", O_RDWR);
    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd); 

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    update_fly_animation(0, w, h, scale);
    init_touch();

    printf("🎙️ [SİSTEM]: Anka OS Aktif, Kovan tam kapasite.\n");

    // --- 3. SÜREKLİ NABIZ DÖNGÜSÜ ---
    while(1) {
        // Ağ bütünlüğü ve Jammer kontrolü
        system("su -c 'python3 agents/net_sync.py --verify'");
        // Nexus nabzı: Sinek asla uyumaz, sürekli gözlemler
        system("su -c 'python3 core/sinek_nexus.py --pulse'");
        
        sleep(5);
    }
    return 0;
}
