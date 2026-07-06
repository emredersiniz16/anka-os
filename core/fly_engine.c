#include <stdio.h>

// Sinek durumları (Terminal yazısı yok, sadece durum kodu var)
typedef enum {
    FLY_IDLE,    // Boşta uçuş
    FLY_THINK,   // El yüz silme / Düşünme
    FLY_WAIT     // Komut bekleme
} FlyState;

FlyState current_state = FLY_IDLE;

void update_fly_behavior() {
    switch(current_state) {
        case FLY_IDLE:
            // Sinek ekranda süzülüyor (Random hareketler)
            break;
        case FLY_THINK:
            // Sinek kondu ve elini yüzünü siliyor (Animasyon tetikleyici)
            break;
        case FLY_WAIT:
            // Sinek butona yakın bekliyor
            break;
    }
}
