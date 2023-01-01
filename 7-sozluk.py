sozluk = {"sıfır":0,"bir":1}
print(type(sozluk))
print(sozluk["bir"])
sozluk["iki"] = 2
print(sozluk)
#? sozluk.keys() sadece anahtarları (soldaki tanımları) alır
#? sozluk.values() sadece değerleri (sağdaki tanımları) alır
#? sozluk.items() bütün sözlük verilerini liste şeklinde alır