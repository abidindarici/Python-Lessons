#veri yapıları - dictionary - sözlük
#sözlüklerde anahtar ve değerler vardır.
#anahtarlar unique olmalıdır.
#anahtarlar immutable olmalıdır.
#anahtarlar string, integer, float, tuple olabilir.
#değerler herhangi bir veri tipi olabilir.
#sözlüklerde sıralama yoktur.
#sözlüklerde index yoktur.
#sözlüklerde eleman sayısı len() fonksiyonu ile bulunur.
#sözlüklerde eleman silme ve değiştirme yapılabilir.
#sözlüklerde eleman ekleme yapılabilir.
#sözlüklerde eleman silme ve değiştirme yapılabilir.

sozluk = {"REG" : "regresyon Modeli", "LOJ" : "lojistik Regresyon", "CART" : "Classification and Reg"}

print(sozluk)

print(sozluk["REG"])

len(sozluk)

sozluk1 = {"REG" : ["RMSE", 10]
              , "LOJ" : ["MSE", 20]
                , "CART" : ["SSE", 30]}
        
print(sozluk1)
