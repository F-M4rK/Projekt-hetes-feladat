def adatok_mentese(fajlnev, adatok):
    # Adatok mentése fájlba
    with open(fajlnev, 'w') as f:
        json.dump(adatok, f, indent=2)
    print(f"Az adatok el lettek mentve a(z) {fajlnev} fájlba.")

# ...

elif valasztas == "2":
    kimeneti_fajlnev = input("Adja meg a kimeneti fájl nevét: ")
    adatok_mentese(kimeneti_fajlnev, adatok)
