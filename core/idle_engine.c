#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// ==========================================
// ANKA OS - BOŞTA BEKLEME (IDLE ENGINE) MOTORU
// ==========================================

// 1. HAYALET GEÇİŞİ EFFECTİ (Ghost Stream)
// İşlemciyi yormadan, sadece Framebuffer satırlarına anlık renk basar
void trigger_ghost_stream(int w, int h) {
    printf("[IDLE] Hayalet veri akışı tetiklendi...\n");
    
    // Ekrandan şimşek hızıyla geçen elektrik mavisi (Siyan) kod satırları simülasyonu
    // fbi veya ağır kütüphaneler yerine doğrudan terminal manipülasyonu yapar
    for(int i = 0; i < 5; i++) {
        // Rastgele bir satır seç ve oraya siberpunk sızıntı efekti bas
        int random_y = rand() % h;
        printf("\033[%d;0H\033[1;36m[SYS_DATA_STREAM_OK] 0x%X -> GLITCH_ACTIVE\033[0m", random_y, rand());
        fflush(stdout);
        usleep(20000); // 20 milisaniye (Göz açıp kapayana kadar)
    }
}

// 2. SİBER RADAR TARAMASI (Cyber Radar & Easter Eggs)
void trigger_cyber_radar(int w, int h) {
    printf("[IDLE] Siber radar taraması başlatıldı...\n");
    
    // Ekranın en köşelerine siberpunk veriler ve gizli kodlar fırlatır
    printf("\033[2;2H\033[1;32m⚡ SYS: ACTIVE\033[0m");
    printf("\033[3;2H\033[1;32m🔋 BAT: ONLINE\033[0m");
    
    // Senin o meşhur WAKE100 kodunu ekranın sağ üst köşesine hayalet gibi gizliyoruz
    printf("\033[2;%dH\033[1;36mPROMO: WAKE100\033[0m", w / 10 - 15);
    fflush(stdout);
    
    usleep(500000); // Yarım saniye ekranda parlasın
    
    // Ekranı temizlemeden sadece o köşeleri tekrar karanlığa gömüyoruz (Eski cihaz dostu)
    printf("\033[2;2H                ");
    printf("\033[3;2H                ");
    printf("\033[2;%dH               ", w / 10 - 15);
    fflush(stdout);
}

// 3. MASTER IDLE MANAGER: Rastgele zamanlarda bu efektleri seçer
void run_idle_orchestrator(int w, int h) {
    int sans = rand() % 100;
    
    if (sans < 15) {
        // %15 ihtimalle ekrandan siber hayalet veri akışı geçecek
        trigger_ghost_stream(w, h);
    } 
    else if (sans >= 15 && sans < 25) {
        // %10 ihtimalle köşelerdeki siber radar ve WAKE100 kodu parlayıp sönecek
        trigger_cyber_radar(w, h);
    }
}
