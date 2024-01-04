print("minden adat listázása: írd be hogy lista")

lista=[]
f=open("fájl.txt.","r",encoding="utf-8")
for sor in f:
    kislista=sor[:-1].split(";")
    lista.append(kislista)
f.close()
