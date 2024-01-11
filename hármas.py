lista = []


with open("évszámok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        kislista = sor[:-1].split(";")
        lista.append(kislista)


evszamok = []
for i in range(1):
    evszam = int(input(f"Kérem, adja meg a(z) {i + 1}. évszámot: "))
    evszamok.append(evszam)


for evszam in evszamok:
    for i in range(len(lista)):
        if lista[i][0] == str(evszam):
            print(f"\nÉvszám: {lista[i][0]}\nTalálmány: {lista[i][1]}\nLeírás: {lista[i][2]}")

