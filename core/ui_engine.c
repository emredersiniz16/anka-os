#include <stdio.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

// --- İMZA MOTORU ---
void render_fly_signature(int x, int y) {
    char sign_cmd[512];
    sprintf(sign_cmd, "fbi -d /dev/fb0 -g 32x32+%d+%d -a -noverbose -T 1 assets/sinek_icon.bmp &", x, y);
    system(sign_cmd);
}

// --- TEMA VE ARAYÜZ ---
void draw_ui_window(const char *message, int is_day) {
    if (is_day) {
        printf("\n[--- YÜKSEK KONTRAST GÜNDÜZ ARAYÜZÜ ---]\n");
        printf("🪰 SİNEK: %s\n", message);
    } else {
        printf("\n[--- SİBERPUNK NEON GECE ARAYÜZÜ ---]\n");
        printf("🪰 SİNEK: %s\n", message);
    }
}

// --- ANA UI RENDER ---
void ui_render(const char *last_message, int sinek_durumu) {
    int fb_fd = open("/dev/fb0", O_RDONLY);
    if (fb_fd < 0) return;
    struct fb_var_screeninfo vinfo;
    ioctl(fb_fd, FBIOGET_VSCREENINFO, &vinfo);
    close(fb_fd);

    int w = vinfo.xres;
    int h = vinfo.yres;
    float scale = (float)w / 1080.0f;
    int is_landscape = (w > h) ? 1 : 0;
    
    time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    int is_day = (tm->tm_hour >= 7 && tm->tm_hour <= 18) ? 1 : 0;

    // 2. SİNEK KONUMLANDIRMA
    char fly_cmd[512];
    if (sinek_durumu == 1) {
        int fx = w/2 - (int)(100*scale);
        int fy = h/2 - (int)(100*scale);
        sprintf(fly_cmd, "fbi -d /dev/fb0 -g 200x200+%d+%d -a -noverbose -T 1 assets/sinek_dusunen.GIF &", fx, fy);
    } else {
        int fx = is_landscape ? (w - (int)(250*scale)) : (w/2 - (int)(75*scale));
        int fy = (int)(50*scale);
        sprintf(fly_cmd, "fbi -d /dev/fb0 -g 150x150+%d+%d -a -noverbose -T 1 assets/sinek_ucuyor.GIF &", fx, fy);
    }
    system(fly_cmd);

    // 4. MESAJ VE İMZA KONTROLÜ
    if (last_message != NULL) {
        char display_msg[1024];
        strcpy(display_msg, last_message);

        if (strstr(display_msg, "[FLY_SIGNATURE_ICON]")) {
            char *ptr = strstr(display_msg, "[FLY_SIGNATURE_ICON]");
            *ptr = '\0'; 
            
            draw_ui_window(display_msg, is_day);
            render_fly_signature(w - 60, h - 60); 
        } else {
            draw_ui_window(display_msg, is_day);
        }
    }
}
