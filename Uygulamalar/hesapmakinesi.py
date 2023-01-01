sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
islem = int(input("Yapmak istediğiniz işlemi seçiniz:\n 1-Toplama\n 2-Çıkarma\n 3-Çarpma\n 4-Bölme\n"))
if(islem>4):
    print("Doğru işlem seçiniz.")
elif(islem==1):
    print(sayi1+sayi2)
elif(islem==2):
    print(sayi1-sayi2)
elif(islem==3):
    print(sayi1*sayi2)
elif(islem==4):
    print(sayi1/sayi2)