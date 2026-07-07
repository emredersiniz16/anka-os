// ui_engine.c (GÜNCELLENMİŞ)

// ... (Diğer fonksiyonlar aynı) ...

// Yeni: İmza İkonunu (Neon Sinek) ekrana basan motor
void render_fly_signature(int x, int y) {
    char sign_cmd[512];
    // İkonu 32x32 boyutunda, tam metnin sonuna veya istediğin koordinata basıyoruz
    sprintf(sign_cmd, "fbi -d /dev/fb0 -g 32x32+%d+%d -a -noverbose -T 1 assets/sinek_icon.bmp &", x, y);
    system(sign_cmd);
}

void ui_render(const char *last_message, int sinek_durumu) {
    // ... (Eski ekran/fb0 kodların buraya gelecek) ...

    // 4. MESAJ VE TEMA (Burada etiketi kontrol edip ikonu basıyoruz)
    if (last_message != NULL) {
        char display_msg[1024];
        strcpy(display_msg, last_message);

        // Eğer mesajın içinde imza etiketi varsa
        if (strstr(display_msg, "[FLY_SIGNATURE_ICON]")) {
            // Etiketi temizle, sadece metni bas
            char *ptr = strstr(display_msg, "[FLY_SIGNATURE_ICON]");
            *ptr = '\0'; 
            
            // Metni bas
            draw_ui_window(display_msg, is_day);
            
            // Neon sinek ikonunu (32x32) metnin hemen yanına veya altına bas
            // Koordinatları ekranın alt kısmına göre dinamik ayarlıyoruz
            render_fly_signature(w - 60, h - 60); 
        } else {
            draw_ui_window(display_msg, is_day);
        }
    }
}
