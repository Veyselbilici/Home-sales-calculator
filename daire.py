ARA_KAT_KATSAYISI =2
UST_KAT_KATSAYISI=1.6
ZEMIN_KAT_KATSAYISI = 0.9

def alani_hesapla(en,boy) :
    alan = en * boy
    return alan

def daire_fiyati_hesapla(kat_katsayisi,alan):
    fiyat = kat_katsayisi * alan * 5000
    return fiyat

en = float(input("en girin: "))
boy =float(input("boy gir: "))

print("lutfen kat seçin")
secim = input("1.ara kat\n2.ust kat\n3.zemin kat\n>>> ")
if secim=="1":
    print("Darenin fiyatı:",daire_fiyati_hesapla(ARA_KAT_KATSAYISI,alani_hesapla(en,boy)))
if secim=="2":
    print("Darenin fiyatı:",daire_fiyati_hesapla(UST_KAT_KATSAYISI,alani_hesapla(en,boy)))
if secim =="3":

    print("Darenin fiyatı:",daire_fiyati_hesapla(ZEMIN_KAT_KATSAYISI,alani_hesapla(en,boy)))
