#calculate body mass index
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def bmi_category(bmi):
    if bmi < 18.5:
        return "Zayıf"
    elif 18.5 <= bmi < 24.9:
        return "Sağlıklı"
    elif 25 <= bmi < 29.9:
        return "Şişman"
    elif 30 <= bmi < 34.9:
        return "1. Derece Obez"
    elif 35 <= bmi < 39.9:
        return "2. Derece Obez"
    else :
        return "3. Derece Obez"

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)
print(f"Vücut Kitle Endeksiniz: {bmi:.2f}")
print(f"Girdiğiniz Sınıf: {category}")