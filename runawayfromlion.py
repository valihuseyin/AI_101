# run away from the lion
def intro():
    print("__________****************__________")
    print("Aslanlardan Kaçış Oyunu'na Hoş Geldiniz!")
    print("Bir ormanda mahsur kaldınız ve bir aslan ile karşılaştınız.")
    print("Amacınız aslandan kaçmak ve hayatta kalmak.")
    print("Ne yaprdınız")
    print("__________****************__________")

def printSecenekler():
    print("1. Kaçardım")
    print("2. Ağaça tırmanırdım")

def printKacisSecenekeleri():
        print("Kaçıyorsunuz...")
        print("Aslan sizi kovalıyor...")
        print("Ne tarafa doğru koşuyorsunuz?")
        print("1. Nehre doğru koşardım")
        print("2. Otoyola doğru koşardım")
def printAgacaTirmanisSecenekeleri():
        print("Ağaça tırmanmaya karar verdiniz...")
        print("Hangi ağaça tırmanırdınız?")
        print("1. En yakın ağaça tırmanırdım")
        print("2. Biraz uzak ama daha uzun ağaça tırmanırdım")

def choose_path():
    path = ""
    while path not in ["1", "2"]:
        path = input("Hangi yolu seçmek istersiniz? (1 veya 2): ")
    return path
def check_path(chosen_path):
    if chosen_path == "1":
        printKacisSecenekeleri()
        chosen_path = choose_path()
        if chosen_path == "1":
            print("Nehre doğru koşuyorsunuz...")
            print("Aslan sizi yakaladı çünkü nehirde timsah var ve siz kararsız kaldınız.")
            print("Oyunu kaybettiniz.")
            return
        elif chosen_path == "2":    
            print("Otoyola doğru koşuyorsunuz...")
            print("Neyse ki arabaları fark edince durdu.")
            print("Tebrikler! Aslandan kaçtınız ve hayatta kaldınız!")
            return
    elif chosen_path == "2":
        printAgacaTirmanisSecenekeleri()
        chosen_path = choose_path()
        if chosen_path == "1":
            print("En yakın ağaça tırmanıyorsunuz...")
            print("Aslan sizi bekliyor ve sizi yakaladı.")
            print("Oyunu kaybettiniz.")
            return
        elif chosen_path == "2":
            print("Daha uzun ağaça tırmanıyorsunuz...")
            print("Aslan sizi bekliyor ama siz ağaçta güvenle duruyorsunuz.")
            print("Aslan pes etti ve gitti.")
            print("Tebrikler! Aslandan kaçtınız ve hayatta kaldınız!")
            return
play_again = "evet"
while play_again.lower() in ["evet", "e"]:
    intro()
    printSecenekler()
    path_number = choose_path()
    check_path(path_number)
    play_again = input("Tekrar oynamak ister misiniz? (evet veya hayır): ")
print("Oyunu oynadığınız için teşekkürler!")    
