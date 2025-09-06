#Girilen "gün", "saat", "dakika" ve "saniye" değerine göre, toplam saniyeyi hesaplayan bir uygulama yapınız
print("Başlama")
gun = int(input("Gün bilgisini giriniz:"))
saat =int(input("Saat bilgisini giriniz:"))
dakika =int(input("Dakika bilgisini giriniz:"))
saniye =int(input("Saniye bilgisini giriniz:"))
print(f"{gun} gün {saat} Saat {dakika} Dakika {saniye} Saniye ")
#saniye += dakika *60
dakika += saat * 60
dakika += gun * 1440
saniye += dakika * 60
print("----------------------------------------------")
print(f"Toplam Saniye: {saniye} dir")