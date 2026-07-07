// security_engine.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Gelecekte eklenecek olan yüz tanıma/parmak izi için bir enum
typedef enum {
    AUTH_PASSWORD,
    AUTH_FINGERPRINT,
    AUTH_FACE
} AuthType;

// Kullanıcının kayıtlı güvenlik yöntemini kontrol eden ana fonksiyon
int authenticate(AuthType type) {
    if (type == AUTH_PASSWORD) {
        char input[32], password[32] = "1234"; // Şifreyi ilerde dosyadan oku
        printf("🔐 [GÜVENLİK] Şifreni gir kanka: ");
        scanf("%s", input);
        return (strcmp(input, password) == 0);
    }
    // Gelecekte buraya AUTH_FINGERPRINT veya AUTH_FACE blokları eklenecek
    return 0;
}

void trigger_lock_mode() {
    printf("🪰 [GÜVENLİK]: Pusu moduna geçiyorum...\n");
    system("clear");
    system("fbi -d /dev/fb0 -a -noverbose assets/lock_screen.bmp &");
    
    // Kilit döngüsü
    while(1) {
        if (authenticate(AUTH_PASSWORD)) {
            printf("Giriş onaylandı kanka, Sinek yuvaya döndü! 🪰\n");
            system("pkill fbi");
            break;
        } else {
            printf("Yanlış kanka, tekrar dene!\n");
        }
    }
}
