"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
sayi = int(input("Kontrol edilecek sayıyı girin: "))
toplam = 0

for i in range(1,sayi):
    if(sayi%i==0):
        toplam += i
if(toplam==sayi):
    print("{} sayısı mükemmel sayıdır.".format(sayi))
else:
    print("{} sayısı mükemmel sayı değildir.".format(sayi))