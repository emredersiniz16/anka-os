#include <stdio.h>
#include <stdlib.h>

// ==========================================
// ANKA OS - DONANIM SES MOTORU (ZERO-STORAGE)
// ==========================================

// 1. KULAK: Sesi mikrofondan alıp RAM'e (geçici hafızaya) kaydeder
void record_audio(int duration_seconds) {
    char cmd[256];
    
    printf("[DONANIM] Mikrofon aktif. %d saniye dinleniyor...\n", duration_seconds);
    
    // arecord: Linux yerleşik ses kaydedicisi.
    // -D plughw:0,0 -> Varsayılan donanım mikrofonu
    // /tmp/anka_voice.wav -> Bu dosya RAM'de tutulur, cihaz hafızasında yer kaplamaz!
    sprintf(cmd, "arecord -D plughw:0,0 -d %d -f cd -t wav /tmp/anka_voice.wav > /dev/null 2>&1", duration_seconds);
    
    // İşletim sistemine komutu yolla ve kaydı başlat
    system(cmd);
    
    printf("[DONANIM] Ses kaydı RAM'e alındı. Buluta yollanmaya hazır.\n");
}

// 2. AĞIZ: Buluttan gelen sesi hoparlöre aktarır
void play_audio(const char* filepath) {
    char cmd[256];
    
    printf("[DONANIM] Hoparlör aktif. Ses oynatılıyor...\n");
    
    // aplay: Linux yerleşik ses oynatıcısı.
    sprintf(cmd, "aplay %s > /dev/null 2>&1", filepath);
    system(cmd);
}
