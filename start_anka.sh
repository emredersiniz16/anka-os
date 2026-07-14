#!/bin/bash

# --- ANKA OS: ANA BAŞLATICI VE BOOT YÖNETİCİSİ (ROOT ZIRHLI) ---

clear
echo "🔊 [ANKA OS]: Sistem kontrol ediliyor..."

# 1. Eğer hazır derlenmiş çekirdek (anka_os) varsa doğrudan çalıştır, yoksa derle
if [ -f anka_os ]; then
    echo "✅ [ANKA OS]: Hazır kovan çekirdeği (anka_os) bulundu. Doğrudan ateşleniyor..."
else
    echo "🔊 [ANKA OS]: Çekirdek bulunamadı! Sistem derleniyor, bekle kanka..."
    # boot.c dosyası core/ klasöründe olduğu için oraya girip derliyoruz
    if [ -f core/boot.c ]; then
        cd core
        if command -v clang &> /dev/null; then
            clang boot.c -o ../anka_os 2>/dev/null
        else
            gcc boot.c -o ../anka_os 2>/dev/null
        fi
        cd ..
    else
        echo "❌ [HATA]: core/boot.c bulunamadı!"
        exit 1
    fi
fi

# Derleme başarılı oldu mu kontrolü
if [ ! -f anka_os ]; then
    echo "❌ [HATA]: Derleme başarısız! Kovan çekirdeği oluşturulamadı."
    exit 1
fi

# Çalıştırma yetkisi ver
chmod +x anka_os
echo "✅ [ANKA OS]: Motor hazır. Ateşleniyor..."
sleep 1

# 2. Boot Logosunu Ekrana Bas (Root yetkisiyle FrameBuffer'a zorla sızıyoruz)
echo "🚀 [SİSTEM]: Anka Logosu ekrana yansıtılıyor..."
pkill -f fbi > /dev/null 2>&1

# DİKKAT: boot.c ile uyumlu olması için assets/sinek_icon.bmp çağırılıyor
su -c "fbi -d /dev/fb0 -a -noverbose -t 3 -1 assets/sinek_icon.bmp" > /dev/null 2>&1

sleep 3
pkill -f fbi > /dev/null 2>&1

# 3. Ana Zeka Motorunu (Ajan Sinek'i) Devreye Sok
echo "🪰 [BİLİNÇ]: Ajan Sinek ROOT zırhıyla uyanıyor..."

# anka_os çekirdeğini doğrudan ROOT (SuperUser) olarak başlatıyoruz!
su -c "./anka_os"
