def isimyazdir(isim,soyisim,*args):
    #buradaki *args pointyer gibi değil değişken sayıda argüman alır, 
    # yani 2 den fazla argüman alabilir, liste gibi davranır 
    print("İsim: ",isim," Soyisim: ",soyisim)
    for i in args:
        print(i)

isimyazdir("Hüseyin","Karadağ",5,"Ankara","Türkiye")

