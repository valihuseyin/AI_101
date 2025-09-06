#Hesap Makinesi Uygulaması v1.0
def islemTipiniAl():
    print("Yapmak istediğiniz işlemi seçin:")
    print("------------------------------------")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("------------------------------------")
    secim = input("Seçiminizi yapın (1/2/3/4): ")
    print("------------------------------------")
    return secim
def sayilariAl():
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    return sayi1, sayi2 
def topla(sayi1, sayi2):
    return sayi1 + sayi2
def cikar(sayi1, sayi2):
    return sayi1 - sayi2
def carp(sayi1, sayi2):
    return sayi1 * sayi2
def bol(sayi1, sayi2):
    if sayi2 != 0:
        return sayi1 / sayi2
    else:
        return "Hata: Bir sayı sıfıra bölünemez."

def hesapla(sayi1, sayi2, secim):
    if secim == '1':
        return topla(sayi1, sayi2)
    elif secim == '2':
        return cikar(sayi1, sayi2)
    elif secim == '3':
        return carp(sayi1, sayi2)
    elif secim == '4':
        return bol(sayi1, sayi2)
    else:
        return "Geçersiz işlem seçimi."
    
secim = islemTipiniAl()
sayi1, sayi2 = sayilariAl()
sonuc = hesapla(sayi1, sayi2, secim)
print(f"Sonuç: {sonuc}")
