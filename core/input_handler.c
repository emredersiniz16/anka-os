#include <stdio.h>

// Bu modül sadece sesli komut ve fiziksel buton girişlerini işler.
// Chat'ten gelen verileri ASLA dinlemez.

void listen_input() {
    printf("--- ANKA OS: Giriş Kontrolcüsü Beklemede ---\n");
    printf("1. Wake-word (Hey Sinek/Click/Anka) dinleniyor...\n");
    printf("2. Kanat (Gönder) butonu dinleniyor...\n");
}

void trigger_ai_process() {
    // Sinek burada "Düşünen Sinek" moduna geçecek
    printf("🪰 Sinek: Düşünme moduna geçildi. (AI aktif)\n");
}
