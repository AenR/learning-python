print("***************\nKullanıcı Girişi\n***************")
kullaniciadi = "aenr"
sifre = "123"

kadigirin = input("Lütfen kullanıcı adınızı giriniz: ")
sifregirin = input("Lütfen şifrenizi giriniz: ")

if(kadigirin==kullaniciadi and sifregirin==sifre):
    print("Sisteme hoş geldiniz!")
else:
    print("Kullanıcı adı veya şifre yanlış!")