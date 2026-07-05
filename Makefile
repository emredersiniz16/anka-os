# ANKA OS - Donanım Derleyicisi
# Cihazın içindeki Android'i silip bizi yazacak binary üretimi

CC=arm-linux-gnueabi-gcc
CFLAGS=-static -Os

all: anka_os.bin

anka_os.bin: core/boot.c
	$(CC) $(CFLAGS) core/boot.c -o anka_os.bin
	@echo "🪰 [SYSTEM]: Anka OS çekirdeği mühürlendi (Binary Hazır)."

clean:
	rm -f anka_os.bin
