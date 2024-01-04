import random


class Vivmany:
    def __init__(self, ev, nev):
        self.ev = ev
        self.nev = nev


def adatok_betoltese(fajlnev):
    adatok = []
    try:
        with open(fajlnev, 'r') as f:
            for sor in f:
                ev, nev = sor.strip().split(',')
                adatok.append(Vivmany(int(ev), nev))
    except FileNotFoundError:
        print("A megadott fájl nem található.")
    return adatok


def tudasteszt(adatok):
    for _ in range(3):
        evszam = random.choice(adatok).év
        helyes_valasz = random.choice([vivmany.nev for vivmany in adatok if vivmany.ev == evszam])

        print(f"Melyik vívmány született {evszam}-ben?")
        valasz = input("Válasz: ")

        if valasz == helyes_valasz:
            print("Helyes válasz!\n")
        else:
            print(f"Helytelen válasz. A helyes válasz: {helyes_valasz}\n")


if __name__ == "__main__":
    fajlnev = "vivmanyok.txt"  # Az adatokat tartalmazó fájl neve
    adatok = adatok_betoltese(fajlnev)

    print("\nTudásteszt kezelő program")
    tudasteszt(adatok)
