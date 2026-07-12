#!/bin/bash

# --- ANKA OS: ANA BAŞLATICI VE BOOT YÖNETİCİSİ (ROOT ZIRHLI) ---

clear
echo "🔊 [ANKA OS]: Sistem derleniyor, bekle kanka..."

# 1. C kodlarını tek bir işletim sistemi çekirdeğine (anka_os) derle
# Arka plandaki karmaşık derleme yazılarını gizle ki şüphe çekmesin.
if command -v clang &> /dev/null; then
    clang boot.c -o anka_os 2>/dev/null
else
    gcc boot.c -o anka_os 2>/dev/null
fi

# Derleme başarılı oldu mu kontrolü
if [ ! -f anka_os ]; then
    echo "❌ [HATA]: Derleme başarısız! Kovan çekirdeği oluşturulamadı."
    exit 1
fi

# Çalıştırma yetkisi ver
chmod +x anka_os
echo "✅ [ANKA OS]: Derleme tamamlandı. Motor ateşleniyor..."
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
