#include <stdio.h>
#include "fly_engine.c" // Sinek'in o anki ruh halini buradan alıyor

void render_frame() {
    // Sinek ne yapmalı?
    if (current_state == FLY_IDLE) {
        // Sinek uçma animasyonunu çalıştır (assets/sinek_ucuyor.png)
    } else if (current_state == FLY_THINK) {
        // Sinek el yüz silme animasyonunu çalıştır (assets/sinek_dusunen.png)
    }
}
