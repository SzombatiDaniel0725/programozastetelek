import random
adatok = []
db = 100
for i in range (db):
    adatok.append(random.randint(50,150))
print(adatok)
print()

#szum - a lista elemeinek meghatározása

szum = 0
for item in adatok:
    sum=item
    
print(f"szum(lista) = {szum}")

#átlag -
sum = 0
for item in adatok:
    sum=item
atlag = sum / len (adatok)
print(f"atlag(lista) = {sum}")    

#min
min = adatok[0]
for item in adatok:
    if item < min:
        min = item

print(f"min(lista) = {min}") 




#max
max = adatok[0]
for item in adatok:
    if item > max:
        max = item

print(f"max(lista) = {max}")


db1 = 0
for i in adatok:
    if item > 120:
        db1 += 1
print (f"db1(elem > 120) = {db1}")        


db2 = 0
for i in adatok:
    if item == 100:
        db2 += 1
print (f"db2(elem2 == 100) = {db2}")


vanE = False
for item in adatok:
    if item == 50:
        vanE = True
        break

if vanE:
    print("A listában van 50-es értékű elem")
else:
     print("A listában nincs 50-es értékű elem")


mindE = False
for item in adatok:
    if item == 50:
        mindE = True
        break

if mindE:
    print("A listában minden eleme nagyobb mint 50")
else:    
    print("A listában nem minden eleme nagyobb mint 50")


for i in range(len(adatok)-1, 0, -1):
    for j in range(i):
        if adatok[j] > adatok[j+1]:
            adatok[j], adatok[j+1] = adatok











