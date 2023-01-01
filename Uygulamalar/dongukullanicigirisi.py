print("***************\nKullanıcı Girişi\n***************")
kullaniciadi = "aenr"
sifre = "123"
giris_hakki = 3
while True:
    kadigirin = input("Lütfen kullanıcı adınızı giriniz: ")
    sifregirin = input("Lütfen şifrenizi giriniz: ")
    
    if(kadigirin==kullaniciadi and sifregirin==sifre):
        print("Sisteme hoş geldiniz!")
        break
    else:
        print("Kullanıcı adı veya şifre yanlış!")
        giris_hakki -= 1
        print("Kalan giriş hakkınız: ",giris_hakki)
    if(giris_hakki==0):
        print("Giriş hakkınız dolduğu için giriş yapamazsınız.")
        break