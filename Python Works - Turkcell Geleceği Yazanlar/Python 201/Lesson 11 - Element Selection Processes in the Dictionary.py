#sözlük eleman işlemleri

sozluk = {"REG" : "regresyon Modeli", "LOJ" : "lojistik Regresyon", "CART" : "Classification and Reg"}


sozlık[0] #hata verir. index yoktur.Sırasız olduğu için.

sozluk["REG"] #anahtar değerine göre eleman seçimi yapılır.

sozluk["REG"]

sozluk = {"REG" : {"RMSE":10, "MSE":20, "SSE":30}, "LOJ" : {"RMSE":10, "MSE":20, "SSE":30}, "CART" : {"RMSE":10, "MSE":20, "SSE":30}}

sozluk["REG"]["RMSE"]
