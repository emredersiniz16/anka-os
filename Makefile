# ANKA OS - Donanım Derleyicisi
# Cihazın içindeki Android'i silip bizi yazacak binary üretimi

CC = arm-linux-gnueabi-gcc
# core/ klasörünü include yoluna ekliyoruz ki #include "ui_engine.c" gibi yollar hata vermesin
CFLAGS = -static -Os -I./core

# Tüm kaynak dosyaların listesi
SRC = core/boot.c

TARGET = anka_os.bin

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $(TARGET)
	@echo "🪰 [SYSTEM]: Anka OS çekirdeği mühürlendi (Binary Hazır)."

clean:
	rm -f $(TARGET)
