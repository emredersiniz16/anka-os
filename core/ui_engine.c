#include <stdio.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <time.h>

// ANSI Renk Kodları (Şimdilik terminal arayüzünü renklendirmek için)
#define GECE_ARKAPLAN "\033[40m"
#define GECE_YAZI "\033[1;36m"    // Neon Camgöbeği (Cyan)
#define GECE_CERCEVE "\033[1;34m" // Elektrik Mavisi

#define GUNDUZ_ARKAPLAN "\033[47m" // Parlak Beyaz Arkaplan
#define GUNDUZ_YAZI "\033[30m"     // Keskin Siyah Yazı
#define GUNDUZ_CERCEVE "\033[34m"  // Koyu Mavi Çerçeve

#define RESET "\033[0m"

// Sinek'in mesajlarını günün saatine göre doğru temayla çizer
void draw_ui_window(const char *message, int is_day) {
    if (is_day) {
        // GÜNDÜZ MODU: Güneşte net görünen yüksek kontrast
        printf("%s%s\n[--- YÜKSEK KONTRAST GÜNDÜZ ARAYÜZÜ ---]%s\n", GUNDUZ_ARKAPLAN, GUNDUZ_CERCEVE, RESET);
        printf("%s%s🪰 SİNEK: %s%s\n", GUNDUZ_ARKAPLAN, GUNDUZ_YAZI, message, RESET);
        printf("%s%s[--------------------------------------]%s\n", GUNDUZ_ARKAPLAN, GUNDUZ_CERCEVE, RESET);
    } else {
        // GECE MODU: Karanlıkta parlayan neon siberpunk
        printf("%s%s\n[--- SİBERPUNK NEON GECE ARAYÜZÜ ---]%s\n", GECE_ARKAPLAN, GECE_CERCEVE, RESET);
        printf("%s%s🪰 SİNEK: %s%s\n", GECE_ARKAPLAN, GECE_YAZI, message, RESET);
        printf("%s%s[------------------------------------]%s\n", GECE_ARKAPLAN, GECE_CERCEVE, RESET);
    }
}

void ui_render(const char *last_message) {
    int fb_fd = open("/dev/fb0", O_RDONLY);
    if (fb_fd < 0) {
        printf("Hata: Donanım tanınamadı.\n");
        return;
    }

    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd);

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    // OTOMATİK TEMA ALGILAYICI (Sistem saatini okur)
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    // Saat sabah 07:00 ile akşam 18:00 arasıysa gündüz modu, değilse gece modu
    int is_day = (tm.tm_hour >= 7 && tm.tm_hour <= 18) ? 1 : 0; 

    if(is_day) {
        printf("☀️ Gündüz Modu Aktif. Cihaz: %dx%d. Ölçek: %.2f\n", w, h, scale);
    } else {
        printf("🌙 Gece Modu (Neon) Aktif. Cihaz: %dx%d. Ölçek: %.2f\n", w, h, scale);
    }
    
    // Eğer Ajan Beyni'nden gelen bir mesaj varsa pencereyi temaya uygun çiz
    if (last_message != NULL) {
        draw_ui_window(last_message, is_day);
    }
}
