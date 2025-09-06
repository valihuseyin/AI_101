
#dictionary : key ve value den oluşur.{} ile tanımlanır.
musteriler = {
       "ad": "Karadag",
      "yaş": 53,
      "şehir": "İstanbul"
    }
dic1 = {} #boş dictionary
dic2 = dict() #boş dictionary
#bir listeye dic de eklenebilir
liste = [1,2,{"ad":"Ali","yaş":30},4]
print(type(liste))
print(liste)
print(liste[2])
#dic içinde dic de olur
musteriler2 = {
       "ad": "Ayşe",
      "yaş": 25,
      "şehir": "Ankara",
      "adres": {
          "sokak": "Atatürk",
          "no": 10,
          "ilçe": "Çankaya"
      }
    }
print(musteriler2["adres"]["sokak"])
#Keys dic keylerini verir
print(musteriler.keys())
for key in musteriler.keys():
    print(key)

#keys döner default, yani keys metotdunu çağırmsakda default key ile döner.
for key in musteriler:
    print(key)
#items dic key value çiftlerini verir
for key,value in musteriler.items():
    print(key,value)

#Values dic value ları verir  
print(musteriler.values())
for value in musteriler.values():
    print(value)

print(type(musteriler))
print(musteriler)
print(musteriler["ad"])
del musteriler["şehir"]
print(musteriler)
musteriler["meslek"] = "Mühendis"
print(musteriler)

#tuple : sıralı ve değiştirilemez veri yapısıdır.() ile tanımlanır.
# tuple de aynı eleman birden fazla olabilir.
# Constan lara benziyor.
# Bir kere oluşturulunca run time da değiştirilemez.
tuple1 = (1, 2, 3, 4, 5)
dir(tuple1) #tuple metotlarını gösterir.
#dir :sahip olduğu metotları gösterir.
print(type(tuple1))
print(tuple1)
print(tuple1[2])#tuple1[2] = 10 #hata verir çünkü tuple değiştirilemez
#----------------
#Set : sırasız ve değiştirilebilir veri yapısıdır.{} ile tanımlanır.
#Set te aynı eleman birden fazla olamaz.  
#dir iöinde veri  tipi veririsek kullanılabilecek metotoşlarıon listesini görürüz.
#Set ler matematikteki küme mantığı ile çalışır.

s = set() #boş set tanımlama
s1 = {} #boş dic tanımlama


set1 = {1, 2, 3, 4, 5}
print(type(set1))   
print(set1)
set1.add(6)
print(set1)
set1.remove(3)
print(set1)
set1.add(4) #aynı elemanı tekrar ekleyemez
print(set1)
set1.add(7)
print(set1) 
#set1.remove(10) #hata verir çünkü 10 elemanı yok
set1.discard(10) #hata vermez
print(set1) 
set1.pop() #rastgele bir elemanı siler
print(set1)
set1.clear() #tüm elemanları siler
print(set1)
print(len(set1)) #eleman sayısını verir
set2 = tuple((1, 2, 3, 4, 5)) #tuple dan sete dönüşüm
print(type(set2))
