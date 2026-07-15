// test_kuantum.c - Anka OS Kuantum Tozu Görsel Test Motoru
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/mman.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <string.h>

// Bizim canavar dokunmatik motorunu içeri alıyoruz
#include "touch_engine.c" 

// Manifestodan: Neon Camgöbeği (Kuantum Tozu Rengi)
#define SEED_COLOR 0x0045A29E 
#define BLACK_GLASS 0x00000000

int main() {
    int fbfd = 0;
    struct fb_var_screeninfo vinfo;
    struct fb_fix_screeninfo finfo;
    long int screensize = 0;
    char *fbp = 0;

    // 1. Ekranın donanım kapısını kır (Framebuffer)
    fbfd = open("/dev/fb0", O_RDWR);
    if (fbfd == -1) {
        printf("Hata: Ekran donanimi (/dev/fb0) acilamadi!\n");
        return 1;
    }

    ioctl(fbfd, FBIOGET_FSCREENINFO, &finfo);
    ioctl(fbfd, FBIOGET_VSCREENINFO, &vinfo);
    screensize = vinfo.yres_virtual * finfo.line_length;

    // Ekranı doğrudan RAM'e haritala (Sıfır gecikme)
    fbp = (char *)mmap(0, screensize, PROT_READ | PROT_WRITE, MAP_SHARED, fbfd, 0);
    
    // Ekranı "Cam Gibi" Zifiri Siyah Yap (Obsidian Dark)
    memset(fbp, 0, screensize);
    printf("🌌 Zifiri cam hazir. Tohumu uyandirmak icin ekrana dokun...\n");

    // Dokunmatik donanımı başlat
    if (init_touch() < 0) return 1;

    int x = 0, y = 0;
    int seed_size = 15; // Tohumun boyutu (Kuantum tozu kalınlığı)

    // 2. Kuantum Nabız Döngüsü (Su gibi akışkan)
    while (1) {
        if (get_touch_event(&x, &y)) {
            // Sadece parmağın olduğu bölgeye Kuantum Tohumunu (Neon Nokta) çiz
            for (int dy = -seed_size; dy <= seed_size; dy++) {
                for (int dx = -seed_size; dx <= seed_size; dx++) {
                    int draw_x = x + dx;
                    int draw_y = y + dy;
                    
                    // Ekran sınırlarını aşmasını engelle
                    if (draw_x >= 0 && draw_x < vinfo.xres && draw_y >= 0 && draw_y < vinfo.yres) {
                        long int location = (draw_x + vinfo.xoffset) * (vinfo.bits_per_pixel / 8) +
                                            (draw_y + vinfo.yoffset) * finfo.line_length;
                        // 32-bit renk basımı (Doğrudan donanıma)
                        *((unsigned int*)(fbp + location)) = SEED_COLOR;
                    }
                }
            }
        }
        usleep(5000); // Ekranı yormadan akışkanlığı sağlamak için mikrosaniyelik dinlenme
    }

    munmap(fbp, screensize);
    close(fbfd);
    return 0;
}
