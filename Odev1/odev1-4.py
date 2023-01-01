"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""
sayi1 = int(input("1. Sayıyı Giriniz: "))
sayi2 = int(input("2. Sayıyı Giriniz: "))
sayi1,sayi2 = sayi2,sayi1
print("Artık 1. sayı= {}, 2.sayı= {}".format(sayi1,sayi2))