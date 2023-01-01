"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""
sayi = int(input("Kontrol edilecek sayıyı girin: "))

if(sayi>999 and sayi<9999):
    dortlu = [int(x) for x in str(sayi)]
    kontrol = dortlu[0]**4+dortlu[1]**4+dortlu[2]**4+dortlu[3]**4
    if(kontrol==sayi):
        print("Sayı armstrongdur.")
    else:
        print("Sayı armstrong değildir.")
        
if(sayi>99 and sayi<999):
    uclu = [int(x) for x in str(sayi)]
    kontrol = uclu[0]**3+uclu[1]**3+uclu[2]**3
    if(kontrol==sayi):
        print("Sayı armstrongdur.")
    else:
        print("Sayı armstrong değildir.")

if(sayi<99 and sayi>9):
    ikili = [int(x) for x in str(sayi)]
    kontrol = ikili[0]**2+ikili[1]**2
    if(kontrol==sayi):
        print("Sayı armstrongdur.")
    else:
        print("Sayı armstrong değildir.")