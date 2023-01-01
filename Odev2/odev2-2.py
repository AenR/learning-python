"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
sayi1 = int(input("1.Sayıyı Girin: "))
sayi2 = int(input("2.Sayıyı Girin: "))
sayi3 = int(input("3.Sayıyı Girin: "))

if(sayi1>sayi2 and sayi1>sayi3):
    print("En büyük {}".format(sayi1))
elif(sayi2>sayi1 and sayi2>sayi3):
    print("En büyük {}".format(sayi2))
elif(sayi3>sayi1 and sayi3>sayi2):
    print("En büyük {}".format(sayi3))