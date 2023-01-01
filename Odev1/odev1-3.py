"""
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""
ad = str(input("Adınız: "))
soyad = str(input("Soyadınız: "))
numara = str(input("Numaranız: "))
bilgi = [ad,soyad,numara]
print("Adınız {} \nSoyadınız {} \nNumaranız {}".format(bilgi[0],bilgi[1],bilgi[2]))