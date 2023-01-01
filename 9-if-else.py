yas = int(input("Yaşınızı Giriniz: "))
if(yas<18):
    print("18 Yaş Altı Giremez!")
else:
    isim = str(input("Adınızı Giriniz: "))
    print("Hoş geldiniz {}!".format(isim))