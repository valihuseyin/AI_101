# Pseudo-code for checking if someone is a crazy cat lover
number_of_cats = int(input("Kaç kediniz var? "))
has_dog = input("Köpeğiniz var mı? (evet/hayır): ").strip().lower() == "evet"

if number_of_cats > 3:
    if has_dog:
        print("Hayvanları seviyor!")
    else:
        print("Kedilere bayılıyor!")
else:
    print("Kedilere deli değiller")
    temperature = int(input("Sıcaklık kaç derece? "))
    is_summer = input("Yaz mevsimi mi? (evet/hayır): ").strip().lower() == "evet"

    if (65 <= temperature <= 90) or (is_summer and 65 <= temperature <= 100):
        print(True)
    else:
        print(False)
