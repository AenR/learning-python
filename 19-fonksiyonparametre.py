# def selamla(name = "Anonim"): #?varsayılan değer verdik(hiçbir değer girilmezse anonim yazacak)
#     print("Merhaba {}! Hoş geldin.".format(name))

# selamla() #?değer girilmesi gereken yer

def toplama(*a):
    toplam = 0
    for i in a:
        toplam += i
    print(toplam)

toplama(1,2,3)