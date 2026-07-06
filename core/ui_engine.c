#include <stdio.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/ioctl.h>

void ui_render() {
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

    printf("Ajan Sinek aktif. Cihaz: %dx%d. Ölçek: %.2f\n", w, h, scale);
    printf("UI: Sinek ve butonlar %dx%d ekranına göre hizalandı.\n", w, h);
}
