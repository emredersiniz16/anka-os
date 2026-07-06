#include <stdio.h>
#include <unistd.h>

// Sinek Animasyon Motoru
// Cihazın ekranına Sinek'in anlık fiziksel durumunu (ASCII/Neon) çizer

void update_fly_animation(int current_state) {
    // 0 = FLY_IDLE (Bekleme Modu)
    if (current_state == 0) {
        // Neon Camgöbeği (Cyan) renk kodu ile Sinek duruşu
        printf("\n\033[1;36m[+] SENSÖRLER AÇIK: Ajan Sinek dinliyor...\033[0m\n");
        printf("\033[1;36m");
        printf("       \\_/\n");
        printf("    -- (0) --\n");
        printf("       / \\\n");
        printf("\033[0m\n");
    } 
    // 1 = FLY_THINK (İşlem / Hack Modu)
    else if (current_state == 1) {
        // Elektrik Mavisi ve Sarı uyarı rengi ile İşlem duruşu
        printf("\n\033[1;33m[⚡] VERİ AĞINA BAĞLANILIYOR / BEYİN İŞLİYOR...\033[0m\n");
        printf("\033[1;34m"); 
        printf("      \\ ⚙️ /\n");
        printf("    == (X) ==\n");
        printf("      / ⚙️ \\\n");
        printf("\033[0m\n");
    }
}
