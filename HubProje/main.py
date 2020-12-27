import time

dersler=["matematik","fizik","programlama","web tasarım",
         "istatistik","kimya","türkçe","tarih"]
s_ders=[]
ogrenciler=set(["mehmet erdem","ömer cengiz","ali cengiz","kutay akalın"])
ogr=input("Ad Soyad\n")
g_sayisi=3
puan={"midterm":60, "final": 50, "project": 80}

def hesapla():
    t_not = (puan["midterm"] * 30 + puan["final"] * 50 + puan["project"] * 20) / 100
    return t_not
while True:
    if ogr.lower() in set(ogrenciler):
        print("Sisteme giriş yapıldı.Hoşgeldin {}".format(ogr))
        time.sleep(0.3)
        print("-DERS LİSTESİ-")
        time.sleep(0.3)

        for i in range(len(dersler)):
            print(dersler[i])
            time.sleep(0.3)
        break

    elif g_sayisi == 0:
        print("HATALI GİRİŞ..."
              "Daha Sonra Tekrar Deneyin...")
        exit()

    else :
        g_sayisi-=1
        print("Öğrenci Kaydı Bulunamadı")
        print("{} hakkınız kaldı.".format(g_sayisi))
        print("Tekrar Giriş Yapın\n")
        ogr = input("Ad Soyad\n")

while True:
    g_ders=input(("LİSTEDEN DERS SEÇİNİZ\n"))
    secme_sayisi = len(s_ders)
    if g_ders.lower() in dersler:
        s_ders.append(g_ders)
        print("{} dersini seçtiniz".format(s_ders))
        secme_sayisi+=1
        print("{} tane ders seçtiniz".format(secme_sayisi))
        kaydet=input("kaydetmet için 'k' tuşuna basın. Devam etmek için 'enter' tuşuna basın\n")
        if kaydet.lower()=="k":
            break

    elif g_ders.lower() not in dersler:
        print("yanlış ders. tekrar girin")

if secme_sayisi<3 or secme_sayisi>5:
    print("BAŞARISIZ OLDUNUZ.'3 ten az ya da 5 ten fazla seçemezsiniz'")
    exit()
if secme_sayisi>=3 or secme_sayisi<=5:
    print(s_ders)
    s_sınav=input("sınav seç\n")
    while True:
        if s_sınav in s_ders:
            hesapla()
            print("sonucunuz {}".format(hesapla()))
        else:
            print("yanlış sınav")
        break

if hesapla()>90:
    print("harf notunuz:AA")
elif 70<hesapla()<90:
    print("harf notunuz:BB")
elif 50<hesapla()<70:
    print("harf notunuz:CC")
elif 30<hesapla()<50:
    print("harf notunuz:DD")
elif hesapla()<30:
    print("harf notunuz:FF")
if hesapla()<30:
    print("ders tekrarı")



