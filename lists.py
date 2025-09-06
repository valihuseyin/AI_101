sayilar = [1,2,3,"Karadag",["a",7]]
print(sayilar)
#index metotu:inex(eleman_adı)--  verilen elemanın indeksini bulur, birden fazla varsa ilk bulduğunu döner
print(sayilar.index(2))
#append :listeye ekleme yapar
sayilar.append(9)
sayilar.append([4,9,5])
print(sayilar)
#extend listeye yeni liste değilde elman eleman eklemek için kullanı
sayilar.extend([7,8,9])
print(sayilar)
#diğer bir extend yöntemi 
print(sayilar+[11,23,45])
#count eleman sayısı
print(sayilar.count(sayilar))
#clear listeyi temizler
sayilar.clear()
#insert : belirtilen index e eleman ekler
sayilar.insert(3,55)
#pop en son da ki elemanı çıkartır, Pop(index )çıkartılacak elemanı 
sayilar.pop()
#remove, çıkarmak istenen elemanı  verirsek onu çıkartır.Birden fazla varsa ilk bulduğunu çıkartır. 
#sayilar.remove(2)
#reverse listeyi ters sıralar
l = [1,2,3,4,5]
print(l.reverse())
#sort :sıralama
lst = [5,3,1,6,77,8,22,33,45]
lst.sort()
lst[2]
print(lst)
l = [1,["Karadag","Alihan"]]
print(l[1][1])
## copy ref bağlantısını koparır
sayilar2 = sayilar.copy()
#range: aralık verir ilk değer alır son değer dail olmaz
a= list(range(1,5))
print(a)