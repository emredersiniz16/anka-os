#include <stdio.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>

// --- TEMA RENKLERİ ---
#define GECE_ARKAPLAN "\033[40m"
#define GECE_YAZI "\033[1;36m"
#define GECE_CERCEVE "\033[1;34m"
#define GUNDUZ_ARKAPLAN "\033[47m"
#define GUNDUZ_YAZI "\033[30m"
#define GUNDUZ_CERCEVE "\033[34m"
#define RESET "\033[0m"

// Sinek'in mesajlarını temaya göre çizer
void draw_ui_window(const char *message, int is_day) {
    if (is_day) {
        printf("%s%s\n[--- YÜKSEK KONTRAST GÜNDÜZ ARAYÜZÜ ---]%s\n", GUNDUZ_ARKAPLAN, GUNDUZ_CERCEVE, RESET);
        printf("%s%s🪰 SİNEK: %s%s\n", GUNDUZ_ARKAPLAN, GUNDUZ_YAZI, message, RESET);
        printf("%s%s[--------------------------------------]%s\n", GUNDUZ_ARKAPLAN, GUNDUZ_CERCEVE, RESET);
    } else {
        printf("%s%s\n[--- SİBERPUNK NEON GECE ARAYÜZÜ ---]%s\n", GECE_ARKAPLAN, GECE_CERCEVE, RESET);
        printf("%s%s🪰 SİNEK: %s%s\n", GECE_ARKAPLAN, GECE_YAZI, message, RESET);
        printf("%s%s[------------------------------------]%s\n", GECE_ARKAPLAN, GECE_CERCEVE, RESET);
    }
}

void ui_render(const char *last_message) {
    // 1. Ekran bilgilerini al
    int fb_fd = open("/dev/fb0", O_RDONLY);
    if (fb_fd < 0) return;
    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd);

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    // 2. Buton Koordinatlarını Hesapla
    int btn_w = (int)(150 * scale);
    int btn_h = (int)(150 * scale);
    int btn_x = w - btn_w - (int)(50 * scale);
    int btn_y = h - btn_h - (int)(50 * scale);

    // 3. Buton Görselini Ekrana Bas
    char cmd[512];
    sprintf(cmd, "fbi -d /dev/fb0 -g %dx%d+%d+%d -a -noverbose -T 1 assets/button.PNG &", btn_w, btn_h, btn_x, btn_y);
    system(cmd);

    // 4. Tema (Saat kontrolü)
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    int is_day = (tm.tm_hour >= 7 && tm.tm_hour <= 18) ? 1 : 0;
    
    // 5. Mesajı Çiz
    if (last_message != NULL) {
        draw_ui_window(last_message, is_day);
    }
}
