"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

boy = float(input("Boyunuzu giriniz(m): "))
kilo = int(input("Kilonuzu giriniz(kg): "))
endeks = kilo/(boy**2)
if(endeks<18.5):
    print("Zayıf")
elif(endeks<25):
    print("Normal")
elif(endeks<30):
    print("Fazla Kilolu")
elif(endeks>30):
    print("Obez")