print("ATM\nİşlemler\n1-Bakiye Sorgulama\n2-Para Yatırma\n3-Para Çekme\n0-Çıkış")
bakiye = 10000

while True:
    islem = input("Yapmak istediğiniz işlemi seçin: ")
    
    if(islem=="0"):
        print("Yine bekleriz.")
        break
    elif(islem=="1"):
        print("Güncel bakiyeniz: ",bakiye)
    elif(islem=="2"):
        a = int(input("Yatırmak istediğiniz miktarı girin: "))
        bakiye += a
    elif(islem=="3"):
        a = int(input("Çekmek istediğiniz miktarı girin: "))
        if(bakiye-a<0):
            print("Yeterli paranız yok.")
        else:
            bakiye -= a
    else:
        print("Geçersiz işlem.")