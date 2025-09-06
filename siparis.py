#restoran
fiyatlar = {"Pizza": 250, "Burger": 350, "Salata": 100}
vergiler={"KDV":0.15,"Bahsis":0.10}

def menu():
    print("----- Menü -----")
    print("1. Pizza - 250 TL")
    print("2. Burger - 350 TL")
    print("3. Salata - 100 TL")
    print("4. Çıkış")
    print("----------------")
    secim = input("Lütfen bir seçenek seçin (1-4): ")
    return secim 
def hesapla_Fiyati(siparis):
    toplam = fiyatlar[siparis]
    toplam += toplam * 0.18  # Vergi ekle %15
    for oran in vergiler.values():
        toplam += toplam * oran
    return toplam

while True:
    secim = menu()
    if secim == "4":
        print("Teşekkür ederiz....")
        print("Güle güle....")
        print("Yine bekleriz...")
        break
    elif secim in ["1", "2", "3"]:
        if secim == "1":
            siparis = "Pizza"
        elif secim == "2":
            siparis = "Burger"
        elif secim == "3":
            siparis = "Salata"
        toplam_fiyat = hesapla_Fiyati(siparis)
        print(f"{siparis} siparişiniz alındı. Toplam fiyat: {toplam_fiyat:.2f} TL")
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")