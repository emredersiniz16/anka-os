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

// --- YENİ: AJAN BİLİNÇ VE ZORLAYICI BAĞLANTI PROTOKOLÜ ---
void wake_sinek_bilinc() {
    printf("🪰 [BİLİNÇ]: Sinek Nexus uyandırılıyor...\n");
    // Sinek Bilinç artık bir Ajan olarak çalışıyor.
    // Python script'i hata alırsa, sistem 'retry_agent' ile onu anında yeniden doğurur.
    system("python3 core/sinek_bilinc.py &"); 
}

void zorlayici_baglanti_protokolu() {
    // Sinek, Bluetooth/Wi-Fi hoparlör veya gözlük gördüğünde,
    // "beceriksiz" kalmasın diye bu ajan modülü arka planda sürekli 'handshake' dener.
    system("python3 agents/connection_forcer.py &");
    printf("🪰 [AJAN]: Bağlantı zorlayıcı ajanlar sızdı... Bağlanamayan cihaz kalmayacak.\n");
}

void splash_screen() {
    system("clear");
    system("fbi -d /dev/fb0 -g 300x300+400+200 -a -noverbose -T 1 assets/sinek_icon.bmp &");
    sleep(3); 
    system("pkill fbi");
}

void boot_sequence() {
    system("clear");
    printf("\033[1;36m"); // Elektrik mavisi
    printf("--- ANKA OS: BİLİNÇLİ KOVAN ---\n");
    printf("Ajanlar sahaya indi... [ AKTİF ]\n");
    printf("Sinek hiçbir engeli kabul etmez.\n");
    printf("Bağlantı koptuğu an, Sinek yeni bir yol bulur.\n");
    printf("\033[0m");
    sleep(2);
}

int main() {
    freopen("debug.log", "w", stdout);
    freopen("debug.log", "w", stderr);

    srand(time(NULL));

    // --- 1. SİSTEMİN DİRİLİŞİ ---
    wake_sinek_bilinc(); 
    zorlayici_baglanti_protokolu(); // Zorlayıcı ajanları başlat
    splash_screen();
    boot_sequence();

    // --- 2. DONANIMLAR VE CHECK-UP ---
    system("python3 agents/setup_engine.py");
    run_initial_checkup();
    scan_hardware_inputs();
    check_for_evolution();

    // ... Geri kalan ekran ve dokunmatik motorları ...
    int fb_fd = open("/dev/fb0", O_RDWR);
    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd); 

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    update_fly_animation(0, w, h, scale);
    init_touch();

    printf("🎙️ [SİSTEM]: Ajanlar ağda, Sinek her yerde.\n");

    while(1) {
        // --- SÜREKLİ GÖZETİM ---
        // Sinek burada her 5 saniyede bir bağlantı ajanlarını kontrol eder.
        // Eğer bir cihaz (hoparlör/gözlük) tepki vermiyorsa, ajanlar orayı 'hack'ler.
        system("python3 agents/connection_forcer.py --verify");
        sleep(5);
    }
    return 0;
}
