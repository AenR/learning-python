from time import sleep
calisanlist = ["Emre","Eren","Tan","Ahmet","Mehmet","Hasan","Hüseyin","Osman","Necati","Muhittin","Şukufe"]
islem = input("Hoş geldiniz. Çalışan listesini getirmek istiyor musunuz? (E/H): ")
if(islem=="E"):
    for calisan in calisanlist:
        print("Çalışan: ",calisan)
        sleep(0.25)
else:
    print("Hoşça kal!")