import time
from anka_installer import run_installation
from anka_orchestrator import AnkaOrchestrator

def main_system_loop():
    # 1. Adım: Cihazı kutudan çıkarıp Android'i sildiğimiz o ilk kurulum anı
    run_installation()
    
    # 2. Adım: İşletim sistemi başarıyla boot edildi, ajanlar hazır
    orchestrator = AnkaOrchestrator()
    
    print("\n" + "="*50)
    print("🛸 ANKA OS CANLI SOHBET ARAYÜZÜ AKTİF")
    print("🤖 'Cihazınız artık tamamen reklamsız ve uygulamasız.'")
    print("🛸 Çıkmak için 'sistemi kapat' yazabilirsiniz.")
    print("="*50 + "\n")

    # 3. Adım: Kullanıcının cihazla yapacağı kesintisiz siberpunk sohbet döngüsü
    while True:
        try:
            user_input = input("🗣️  Kullanıcı: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["sistemi kapat", "exit", "quit"]:
                print("\n🪰  [ANKA OS]: Bzzz... *CLICK* -> Sistem güvenli modda kapatıldı.")
                break

            # Kullanıcı cihazla sohbet ediyor, orkestratör emri bölüp ajanlara dağıtıyor
            orchestrator.process_command(user_input)
            print("\n" + "-"*50 + "\n")
            
        except KeyboardInterrupt:
            print("\n🪰  [ANKA OS]: Acil durum kernel kilidi devreye girdi.")
            break

if __name__ == "__main__":
    main_system_loop()
