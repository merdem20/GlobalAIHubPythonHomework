import time

isim = input("adınızı giriniz\n")
soyad = input("soyadınızı giriniz\n")
yas = int(input("yaşınızı giriniz\n"))
d_tarih = int(input("doğum yılınızı giriniz (sadece yıl)\n"))
k_liste = [isim,soyad,yas,d_tarih]
for i in k_liste:
    print(i)

time.sleep(1)
if yas<18:
    print("sokağa çıkmak tehlikeli")

else :
    print("sokağa çıkmak güvrnli")
