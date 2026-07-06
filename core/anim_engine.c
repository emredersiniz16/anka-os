#include <stdio.h>

// Artık koca koca render kodları yok, sadece dosya yolu ve oynatma var.
void play_animation(const char* gif_name) {
    // Sistem, donanımın video decoder'ını kullanarak gif'i tetikler.
    printf("--- ANKA OS: Animasyon Oynatılıyor: %s ---\n", gif_name);
    // Donanım seviyesinde: system("play_gif /assets/%s", gif_name);
}

// Sinek durumuna göre sadece gif çağırıyoruz
void update_fly_animation(int state) {
    if (state == 0) { // FLY_IDLE
        play_animation("sinek_ucuyor.gif");
    } else if (state == 1) { // FLY_THINK
        play_animation("sinek_dusunen.gif");
    }
}
