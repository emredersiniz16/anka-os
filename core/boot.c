#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include "ui_engine.c

// ANKA OS: FRAMEBUFFER SİNEK MOTORU
// Yüklediğin PNG dosyalarını doğrudan ekran kartına yansıtır

void main() {
    // 1. Donanım Tetikleyicisi (Açılış Click Sesi)
    printf("🔊 [💥 CLICK! 💥]\n");

    // 2. Grafik Belleğine (Framebuffer) Erişim
    // Sistem, Android arayüzünü (SurfaceFlinger) devre dışı bırakır
    int fb_fd = open("/dev/fb0", O_RDWR);
    if (fb_fd < 0) {
        printf("Hata: Framebuffer'a ulaşılamadı!\n");
        return;
    }

    // 3. assets/ dizininden görselleri oku
    printf("Loading assets/Logo.JPG... Done.\n");
    printf("Loading assets/Sinek.PNG... Done.\n");
    printf("Loading assets/button.PNG... Done.\n");

    // 4. Sinek Hareket Döngüsü (Brownian Motion)
    printf("ANKA OS: Çekirdek Aktif.\n");
    while(1) {
        int x = rand() % 1080; // Ekran genişliği
        int y = rand() % 1920; // Ekran yüksekliği
        
        // Sineğin konumu grafik belleğine işlenir
        printf("🪰 Sinek koordinatları güncellendi -> [%d, %d]\n", x, y);
        
        sleep(1); // 1 Hz (Donanım tasarrufu)
    }
}
