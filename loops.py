#  for in 
for num in list(range(1,10)):
    print(num)
for num in range(10,17):
    if num ==  15:
        break
    print(num)
#continue : bir sonraki döngünün adımına geçer
for h in "hüseyin karadağ":
    if h != "h":
        continue
    print(f"İsmin harfleri : {h}")

#break : döngüden çıkar
                
#while
deger = 10

while deger>0:
    print(deger)
    deger -= 1
    if deger == 3:
        break
deger = 10
while deger>0:
    print(deger)
    deger *= 3
    if deger == 30:
        break
deger = 1
while deger>0:
    print(deger)
    deger += 3
    if deger == 10:
        break

isimler = ["Ege","Zafer","Ege","Alihan"]
while "Ege" in isimler: # burada listede contains kontrolü yapıyor 
    isimler.remove("Ege")

print(isimler)
isimler = ["Ege","Zafer","Ege","Alihan"]
print(isimler)

isimler = ["Ege","Zafer","Ege","Alihan"]
for a in isimler:
    if a == "Ege":
        isimler.remove(a)

print(isimler)
for "Ege" in isimler:
    isimler.remove("Ege")
print(isimler)
