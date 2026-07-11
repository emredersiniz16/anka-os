import subprocess

def run_evrim():
    # 'core' klasöründeki zekayı al ve cihazın super bölümüne enjekte et
    print("Kovan uyanıyor... Enjeksiyon başlıyor.")
    subprocess.run(["python", "../core/evrim_motoru.py", "--payload", "universal_sinek.bin"])

def run_bakim():
    # Sadece temel temizlik
    subprocess.run(["fastboot", "format", "userdata"])
    print("Sistem temizlendi.")

# Telefoncu sadece butona basacak
print("Anka OS - Dükkan Operatörü")
action = input("1: Evrim, 2: Bakım: ")
if action == "1": run_evrim()
else: run_bakim()
