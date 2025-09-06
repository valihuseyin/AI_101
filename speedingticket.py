"""
1. Eğer doğum gününse, hız sınırlarını 5 arttır.
2. Eğer hızın 65 veya daha az ise:
    - Ceza yok.
3. Eğer hızın 65'ten fazla ve 80 veya daha az ise:
    - Küçük ceza.
4. Eğer hızın 80'den fazla ise:
    - Büyük ceza.
"""
# Pseudo-code for speeding ticket calculation
speed = int(input("Enter your speed: "))
is_birthday = input("Is it your birthday? (yes/no): ").strip().lower() == "yes"
if is_birthday:
    speed -= 5  # Increase speed limit by 5 on birthday 
if speed <= 65:
    print("No ticket")
elif 66 <= speed <= 80:
    print("Small ticket")
else:
    print("Big ticket")
# Pseudo-code for speeding ticket calculation
num = 2
while num <= 20:
    print(num)
    num += 2

# Alternatif olarak range ile:
for num in range(2, 21, 2):
    print(num)

# 10'dan 1'e kadar for döngüsü ile:
for num in range(10, 0, -1):
    print(num)
print("Blastoff!")
