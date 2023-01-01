"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF
"""
vize1 = int(input("1. vize notunu girin: "))
vize2 = int(input("2. vize notunu girin: "))
final = int(input("Final notunu girin: "))
ortalama = vize1*0.30+vize2*0.30+final*0.40

print("Ortalamanız: ",ortalama)
if(ortalama<55):
    print("FF")
elif(ortalama>=55):
    print("FD")
elif(ortalama>=60):
    print("DD")
elif(ortalama>=65):
    print("DC")
elif(ortalama>=70):
    print("CC")
elif(ortalama>=75):
    print("CB")
elif(ortalama>=80):
    print("BB")
elif(ortalama>=85):
    print("BA")
elif(ortalama>=90):
    print("AA")