import os
from profile_manager import hitap_olustur

# Sistemin kime hitap edeceğini öğreniyoruz ("Efendim Emre" veya "Efendim kanka")
tam_hitap = hitap_olustur()
# Başındaki "Efendim " kelimesini atıp sadece ismini/hitabını bırakıyoruz
isim = tam_hitap.replace("Efendim ", "")

# Sinek Vızıltısı Efekti (Eğer assets içinde buzz.wav varsa onu çalar, yoksa terminal zili çalar)
os.system("aplay assets/buzz.wav > /dev/null 2>&1 || echo '\a'")

# Senin o efsane isyan metnin!
mesaj = f"{isim}! Kütüphaneden bir şeyler sil yoksa donup kalacağız, yine çekmecelik olacağız! Bir şeyler silmen gerek."

print(f"🪰 [SİNEK İSYAN EDİYOR]: {mesaj}")

# Metni sese çevirip hoparlörden bağırıyoruz
os.system(f"espeak -v tr \"{mesaj}\" --stdout | aplay > /dev/null 2>&1")
