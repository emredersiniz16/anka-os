#!/bin/bash

# ANKA OS - ANA BAŞLATICI VE BOOT YÖNETİCİSİ

clear
echo "🔊 [ANKA OS] Sistem derleniyor, bekle kanka..."

# 1. C kodlarını tek bir işletim sistemi çekirdeğine (anka_os) derle
# Cihazda clang veya gcc hangisi varsa onu otomatik bulup kullanır
if command -v clang &> /dev/null; then
    clang boot.c -o anka_os
else
    gcc boot.c -o anka_os
fi

# Derleme başarılı oldu mu kontrolü
if [ ! -f anka_os ]; then
    echo "❌ HATA: Derleme başarısız! C kodlarında bir eksik var."
    exit 1
fi

# Çalıştırma yetkisi ver
chmod +x anka_os
echo "✅ [ANKA OS] Derleme tamamlandı. Motor ateşleniyor..."
sleep 1

# 2. Boot Logosunu Ekrana Bas (Cihazın kendi orijinal açılışı gibi)
echo "🚀 Logo ekrana yansıtılıyor..."
pkill -f fbi > /dev/null 2>&1
# Logo.JPG dosyasını tam ekran (framebuffer) olarak 3 saniye gösterir
fbi -d /dev/fb0 -a -noverbose -t 3 -1 assets/Logo.JPG > /dev/null 2>&1

sleep 3
pkill -f fbi > /dev/null 2>&1

# 3. Ana Zeka Motorunu (Ajan Sinek'i) Devreye Sok
echo "🪰 Ajan Sinek uyanıyor..."
./anka_os
