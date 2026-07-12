// security_engine.c - GÜNCELLEDİM
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

typedef enum { AUTH_PASSWORD, AUTH_FINGERPRINT, AUTH_FACE } AuthType;

// Kullanıcının kayıtlı güvenlik yöntemini kontrol eden ana fonksiyon
int authenticate(AuthType type) {
    if (type == AUTH_PASSWORD) {
        char input[32], password[32] = "1234";
        printf("🔐 [GÜVENLİK] Şifreni gir kanka: ");
        scanf("%s", input);
        return (strcmp(input, password) == 0);
    }
    return 0;
}

void trigger_lock_mode() {
    printf("🪰 [GÜVENLİK]: Pusu moduna geçiyorum...\n");
    
    // 1. Kilit moduna geçerken arka planda "Sinek Nexus"u canlı tut
    // Bu sayede kilitli olsa bile sistem donanımı izlemeye devam eder
    system("./start_anka.sh --silent &");
    
    system("clear");
    system("fbi -d /dev/fb0 -a -noverbose assets/lock_screen.bmp &");
    
    // Kilit döngüsü
    while(1) {
        // Döngü içerisinde Sinek'in nabzını (rejenere) koru
        system("./core/rejenere_motoru.py --check-status"); 
        
        if (authenticate(AUTH_PASSWORD)) {
            printf("Giriş onaylandı kanka, Sinek yuvaya döndü! 🪰\n");
            system("pkill fbi");
            // Kilit kalkınca Nexus'u tam kapasiteye al
            system("./start_anka.sh --full-power &");
            break;
        } else {
            printf("Yanlış kanka, tekrar dene!\n");
            // Yanlış denemede sistemi "Pusu" modunda tut
            system("sleep 2");
        }
    }
}
