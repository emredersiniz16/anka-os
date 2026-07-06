#include <stdio.h>

int get_battery_level() {
    FILE *fp = fopen("/sys/class/power_supply/battery/capacity", "r");
    if (fp == NULL) {
        // Eğer cihazda o yol yoksa, şarjı okuyamıyorsa en azından statik 100 dönmesin, 
        // sisteme "okunamadı" uyarısı versin.
        return -1; 
    }
    int capacity;
    fscanf(fp, "%d", &capacity);
    fclose(fp);
    return capacity;
}
