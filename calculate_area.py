t = int(input("Alanını hesaplamak istediğiniz çokgen tipini Giriniz \n Üçgen:1 \n Dörtgen:2\n Daire:3\n"))
print(f"Çokgen Tİpi: {t}")

if  t== 3:
    pi = 3.14
    r = int(input("Yarıçap Bilgisini Giriniz:"))
    print(f"Dairenin alanı:{r**2 * pi}")
else :

#take height
    h = int(input("Yüksekliği Giriniz:"))
#print(f"Yükseklik : {h}")
    l = int(input("En Uzunluğunu Giriniz:"))
#print(f"En Uzunluğu: {l}")

    alan = 0
    if t == 1:
        alan = (l * h )/2 
        print(f"Üçgenin alanı:{alan}")
    elif t == 2:
        alan = l * h
        print(f"Dörtgenin alanı:{alan}")