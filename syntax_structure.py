x, y = 5,10
if x < y:
    print("x yden küçüktür.")

print(2== 3)
try:
    number = int(input("Bir Sayı giriniz:"))
    if number > 100:
        print("Girdiğiniz sayı 100 den büyüktür.")
    elif number < 100:
        print("Girdiğiniz sayı 100 den küçüktür.")
    else:
        print("Girdiğiniz sayı 100 e eşittir.")
except ValueError:
    print("Girdiğiniz değer sayı değil.")