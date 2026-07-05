#include <stdio.h>
#include <unistd.h>

// Android'in tüm arayüz katmanlarını (SurfaceFlinger) devre dışı bırakıyoruz.
// Sadece donanım (framebuffer) ile konuşan saf terminal.

void main() {
    // 1. Click sesini donanım portundan gönder (Sistemin uyanış sesi)
    printf("🔊 [💥 CLICK! 💥]\n");

    // 2. Ekranı tamamen temizle (Siyah boşluk)
    system("clear");
    printf("--- ANKA OS: SİSTEM BAŞLADI ---\n");

    // 3. Sinek döngüsünü başlat (1Hz ile donanımı yormadan)
    while(1) {
        printf("🪰 [Sinek Gözlemi: X:500, Y:500]\n");
        sleep(1); // 1 Hz ritmi
    }
}
