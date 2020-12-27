import random
def game():
    number=random.randrange(0,25)
    k_number=int(input("0-25 arası fasayıyı tahmin ediniz\n"))

    sans=3

    while True:
        if sans!=0:
            if k_number<number:
                sans-=1
                print(sans, "hakkınız kaldı")
                k_number = int(input(("""sayıyı büyült
    Tekrar sayı girin\n""")))

            elif k_number>number:
                sans -= 1
                print(sans, "hakkınız kaldı")
                k_number = int(input(("""sayıyı küçült
    Tekrar sayı girin\n""")))

            if k_number==number:
                print("tebrikler doğru tahmin")
                break
            if sans==0:
                print("hakkınız bitti 'KAYBETTİNİZ'")
                print("Sayı:",number)
                break

isim = input("adınızı giriniz\n")
soyad = input("soyadınızı giriniz\n")
yas = int(input("yaşınızı giriniz\n"))
d_tarih = int(input("doğum yılınızı giriniz (sadece yıl)\n"))
k_liste=[isim,soyad,yas,d_tarih]
if len(k_liste)==4:
    print("OYUNA HOŞGELDİNİZ",isim)
    game()
else:
    print("eksik bilgi")
