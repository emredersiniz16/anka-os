import json
import os

PROFILE_FILE = "profile.json"

def profil_yukle():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)
    return {"isim": "Kullanıcı", "hitap": "kanka"}

def profil_kaydet(isim, tercih):
    with open(PROFILE_FILE, "w") as f:
        json.dump({"isim": isim, "hitap": tercih}, f)

def hitap_olustur():
    p = profil_yukle()
    if p["hitap"] == "isim":
        return f"Efendim {p['isim']}"
    return "Efendim kanka"
