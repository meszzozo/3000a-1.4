lista=[]

with open("03.000.txt" ,"r", encoding="utf8") as f:
    for i in f:
        lista.append(szam)


print("fájl bezárva")
print(f"1.Hány eleme van a sorozatnak{len(lista)}")
print(f"2. Van-e negatív szám")

for