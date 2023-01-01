"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m)*Boy(m)
"""
boy = float(input("Boyunuzu giriniz(m): "))
kilo = int(input("Kilonuzu giriniz(kg): "))
print(kilo/(boy**2))