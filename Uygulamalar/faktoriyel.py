# faktoriyel = 1
# sayac = 1
# sayi = int(input("Faktöriyeli bulunacak sayıyı girin: "))
# while(sayac<sayi):
#     sayac += 1
#     faktoriyel *= sayac
# print("Cevap: ",faktoriyel)

while True:
    sayi = int(input("Faktöriyeli bulunacak sayıyı girin (çıkış için 0): "))
    if(sayi==0):
        print("Programdan çıkılıyor.")
        break
    else:
        faktoriyel = 1
        for i in range(2,sayi+1):
            faktoriyel *= i
    print("Cevap: ",faktoriyel)