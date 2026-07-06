#include <stdio.h>
#include <stdlib.h>

// ==========================================
// ANKA OS - GÖRME VE KÜTÜPHANE MOTORU
// ==========================================

void capture_image() {
    printf("[DONANIM] Sinek gözünü açtı. Çevreyi tarıyor...\n");
    
    // Sistemde 'gallery' adında bir klasör yoksa otomatik oluşturur
    system("mkdir -p gallery"); 
    
    // Fotoğrafı geçici hafızaya değil, kalıcı kütüphaneye saniye damgasıyla kaydet
    // Örnek: gallery/foto_1718293847.jpg
    system("fswebcam -r 1280x720 --no-banner gallery/foto_$(date +%s).jpg > /dev/null 2>&1");
    
    printf("[DONANIM] Görüntü başarıyla kütüphaneye eklendi.\n");
}
