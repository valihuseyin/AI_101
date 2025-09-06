#cevap = int(input("5+5 sonucu nedir?"))
#if cevap== 10:
#    print("Congrats")
#else:
#    print(":(")
isimler = ["huseyin","fbk","alihan","hatice kübra","zk"]
if "zk" in isimler:
    print("bulundu")

if "Fatma" not in isimler:
    print("Fatma listede dğeildir.")

isim = "karadag"

if "ğ" in isim:
    print("ğ {} da var".format(isim))
elif "l" in isim:
    print("g {} da var.".format(isim))
else:
    print(f"isim:{isim}")


x = 6
y= x == 5
if not y:
    print("x 5 değildir.")