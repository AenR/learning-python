# liste1 = range(15)
# liste2 = []

# for i in liste1:
#     liste2.append(i)

# print(liste2)

liste1 = range(6)
liste2 = [i for i in liste1]
print(liste2)

liste = [(1,2),(3,4),(5,6)]
liste3 = [a*b for a,b in liste]
print(liste3)

#? Bir listenin verilerini diğer listeye geçirmenin kısa yolu