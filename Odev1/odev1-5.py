"""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""
dik1 = int(input("Dik kenarı girin: "))
dik2 = int(input("Diğer Dik kenarı girin: "))
hipotenus = int((dik1**2+dik2**2)**0.5)
print("Üçgenin kenarları: {} {} Hipotenüsü: {}".format(dik1,dik2,hipotenus))