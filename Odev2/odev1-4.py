"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
"""

islem = str(input("Hesaplama yapmak istediğiniz işlemi yazın(üçgen/dörtgen): "))

if(islem=="üçgen"):
    kenar1 = int(input("1. kenarı giriniz: "))
    kenar2 = int(input("2. kenarı giriniz: "))
    kenar3 = int(input("3. kenarı giriniz: "))
    if(kenar1+kenar2>kenar3 and kenar2+kenar3>kenar1 and kenar1+kenar3>kenar2):
        if(kenar1==kenar2==kenar3):
            print("Girdiğiniz kenarlar bir eşkenar üçgene ait.")
        elif((kenar1==kenar2 and kenar1!=kenar3) or (kenar1==kenar3 and kenar1!=kenar2) or (kenar2==kenar3 and kenar2!=kenar1)):
            print("Girdiğiniz kenarlar bir ikizkenar üçgene ait.")
        else:
            print("Girdiğiniz değerler bir üçgene ait.")
    else:
        print("Girdiğiniz kenarlar bir üçgen belirtmiyor.")
elif(islem=="dörtgen"):
    kenar1 = int(input("1. kenarı giriniz: "))
    kenar2 = int(input("2. kenarı giriniz: "))
    kenar3 = int(input("3. kenarı giriniz: "))
    kenar4 = int(input("4. kenarı giriniz: "))
    if(kenar1==kenar2==kenar3==kenar4):
        print("Girdiğiniz kenarlar bir kareye ait.")
    elif(kenar1==kenar3 and kenar2==kenar4):
        print("Girdiğiniz kenarlar bir dikdörtgene ait.")
    else:
        print("Girdiğiniz kenarlar bir dörtgene ait.")
else:
    print("Lütfen verilen işlemlerden birini seçin.")