#include <stdio.h>
#include <stdlib.h>

// ==========================================
// ANKA OS - CANLI GÖZ VE VİZYON MOTORU
// ==========================================

// 1. ANLIK ÇEKİM (Zeka Analizi İçin)
void capture_image() {
    printf("[DONANIM] Sinek gözünü kırptı. Fotoğraf çekiliyor...\n");
    system("mkdir -p gallery"); 
    // Fotoğrafı çeker ve kütüphaneye atar (Zeka ajanı bu son fotoğrafı alıp inceleyecek)
    system("fswebcam -r 1280x720 --no-banner gallery/son_bakis.jpg > /dev/null 2>&1");
    printf("[DONANIM] Görüntü alındı. AI analizi için hazır.\n");
}

// 2. CANLI KAMERA AÇ (Canlı Akış)
void open_live_camera() {
    printf("👁️ [GÖZ]: Canlı yayın başlatılıyor...\n");
    // Linux'un yerleşik video motoru 'ffmpeg' ile kamerayı doğrudan ekrana (fb0) basıyoruz. 
    // Sonundaki '&' işareti bunun arka planda sürekli çalışmasını sağlar.
    system("ffmpeg -f v4l2 -framerate 30 -video_size 640x480 -i /dev/video0 -pix_fmt bgra -f fbdev /dev/fb0 > /dev/null 2>&1 &");
}

// 3. CANLI KAMERA KAPAT
void close_live_camera() {
    printf("👁️ [GÖZ]: Canlı yayın kapatılıyor...\n");
    // Arka planda çalışan canlı yayını öldürür
    system("killall ffmpeg > /dev/null 2>&1");
    system("clear"); // Sinek'in geri gelmesi için ekranı temizle
}
