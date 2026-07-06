    while(1) {
        // Kullanıcıdan gelen metin
        char gelen_mesaj[] = "yükselt"; 
        
        printf("🪰 Beyin tetikleniyor: '%s'\n", gelen_mesaj);

        // 1. Zeka Devrede: C içinden Python Ajan Beynini çağır ve çıktıyı yakala
        char command[512];
        sprintf(command, "python3 agents/fly_brain.py \"%s\"", gelen_mesaj);
        
        FILE *fp = popen(command, "r");
        if (fp != NULL) {
            char path[1024];
            // Python'dan gelen her satırı tek tek yakalayıp ekrana basıyoruz
            while (fgets(path, sizeof(path), fp) != NULL) {
                printf("%s", path); 
            }
            pclose(fp);
        }
        
        // 2. Animasyon Devrede: Düşünme modunu tetikle
        current_state = 1; // FLY_THINK
        update_fly_animation(current_state);

        printf("🪰 Ajan Sinek zeka ağında karar veriyor.\n");
        
        sleep(5); 
    }
