#include <stdio.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include "../system_monitor.c" // 👈 İşte eksik parça burada, bunu ekle!

// --- TEMA RENKLERİ ---
#define GECE_ARKAPLAN "\033[40m"
#define GECE_YAZI "\033[1;36m"
#define GECE_CERCEVE "\033[1;34m"
#define GUNDUZ_ARKAPLAN "\033[47m"
#define GUNDUZ_YAZI "\033[30m"
#define GUNDUZ_CERCEVE "\033[34m"
#define RESET "\033[0m"

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

// Sinek durumu 0: Uçuyor, 1: Düşünüyor
void ui_render(const char *last_message, int sinek_durumu) {
    int fb_fd = open("/dev/fb0", O_RDONLY);
    if (fb_fd < 0) return;
    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd);

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;

    // 1. ÜST PANEL (Şarj ve Saat)
    // get_battery_level() artık system_monitor.c üzerinden geliyor
    int batt = get_battery_level();
    time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    
    if (batt != -1)
        printf("\n[PANEL] 🔋 %d%% | ANKA OS | %02d:%02d\n", batt, tm->tm_hour, tm->tm_min);
    else
        printf("\n[PANEL] 🔋 --%% | ANKA OS | %02d:%02d\n", tm->tm_hour, tm->tm_min);

    // 2. SİNEK KONUMLANDIRMA (Duruma göre)
    char fly_cmd[512];
    if (sinek_durumu == 1) { // Düşünürken ortaya gel
        int fx = w/2 - (int)(100*scale);
        int fy = h/2 - (int)(100*scale);
        sprintf(fly_cmd, "fbi -d /dev/fb0 -g 200x200+%d+%d -a -noverbose -T 1 assets/sinek_dusunen.GIF &", fx, fy);
    } else { // Uçarken sağ üste git
        int fx = w - (int)(250*scale);
        int fy = (int)(50*scale);
        sprintf(fly_cmd, "fbi -d /dev/fb0 -g 150x150+%d+%d -a -noverbose -T 1 assets/sinek_ucuyor.GIF &", fx, fy);
    }
    system(fly_cmd);

    // 3. BUTON ÇİZİMİ
    int btn_w = (int)(150 * scale);
    int btn_h = (int)(150 * scale);
    int btn_x = w - btn_w - (int)(50 * scale);
    int btn_y = h - btn_h - (int)(50 * scale);
    char btn_cmd[512];
    sprintf(btn_cmd, "fbi -d /dev/fb0 -g %dx%d+%d+%d -a -noverbose -T 1 assets/button.PNG &", btn_w, btn_h, btn_x, btn_y);
    system(btn_cmd);

    // 4. MESAJ VE TEMA
    int is_day = (tm->tm_hour >= 7 && tm->tm_hour <= 18) ? 1 : 0;
    if (last_message != NULL) {
        draw_ui_window(last_message, is_day);
    }
}
