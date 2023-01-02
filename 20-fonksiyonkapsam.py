b = 3 #globaldeki b

def fonksiyon():
    global b #globaldeki b'yi seçtik
    b += 3
    a = 10
    print(a) #local değişken
    print(b)

fonksiyon()
#print(a) #a global olmadığı için yazdırmaz

a = 20 #global değişken
print(a)

#! if ve while içinde tanımlanan değişkenler de global değişken