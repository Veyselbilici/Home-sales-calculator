from arsa import *
from daire import *
while True:
    print("1. Arsa için fiyat hesapla")
    print("2. Daire için fiyat hesapla")
    print("h. Çıkış yap")
    secim = input("1. Arsa için fiyat\n2. Daire için fiyat\nh. Çıkış yap\n>>> ")

    if secim == "1":
        DENIZ_KENARI = 1.6
        SEHIR_MERKEZI = 1.2
        KIRSAL = 0.8

        def arsa_cevresi(secim, en=0, boy=0, yaricap=0):
            if secim == "dikdortgen":
                return 2 * (boy + en)
            elif secim == "cember":
                return 2 * 3.14 * yaricap

        def arsa_fiyati_hesapla(bolge_katsayisi, arsa_cevresi):
            return bolge_katsayisi * arsa_cevresi * 1000

        print("Lütfen arsanın konumunu seçin:")
        print("1 - Deniz kenarı")
        print("2 - Şehir merkezi")
        print("3 - Kırsal")
        bolge_secimi = input("Seç (1/2/3): ")

        if bolge_secimi == "1":
            bolge_katsayisi = DENIZ_KENARI
        elif bolge_secimi == "2":
            bolge_katsayisi = SEHIR_MERKEZI
        elif bolge_secimi == "3":
            bolge_katsayisi = KIRSAL

        print("Arsa şeklini seçin:")
        print("1 - Dikdörtgen")
        print("2 - Çember")
        sekil_secimi = input("Seç (1/2): ")

        if sekil_secimi == "1":
            en = float(input("Dikdörtgenin eni: "))
            boy = float(input("Dikdörtgenin boyu: "))
            arsa_cevresi = arsa_cevresi("dikdortgen", en=en, boy=boy)
        elif sekil_secimi == "2":
            yaricap = float(input("Çemberin yarıçapı: "))
            arsa_cevresi = arsa_cevresi("cember", yaricap=yaricap)

        arsa_fiyati = arsa_fiyati_hesapla(bolge_katsayisi, arsa_cevresi)

        print(f"Arsanın fiyatı: {arsa_fiyati} TL")

    elif secim == "2":
        ARA_KAT_KATSAYISI = 2
        UST_KAT_KATSAYISI = 1.6
        ZEMIN_KAT_KATSAYISI = 0.9

        def alani_hesapla(en, boy):
            alan = en * boy
            return alan

        def daire_fiyati_hesapla(kat_katsayisi, alan):
            fiyat = kat_katsayisi * alan * 5000
            return fiyat

        en = float(input("Eni girin: "))
        boy = float(input("Boyu girin: "))
        print("Lütfen kat seçin")
        secim = input("1.ara kat\n2.ust kat\n3.zemin kat\n>>> ")
        if secim=="1":
         print("Darenin fiyatı:",daire_fiyati_hesapla(ARA_KAT_KATSAYISI,alani_hesapla(en,boy)))
        if secim=="2":
         print("Darenin fiyatı:",daire_fiyati_hesapla(UST_KAT_KATSAYISI,alani_hesapla(en,boy)))
        if secim =="3":

          print("Darenin fiyatı:",daire_fiyati_hesapla(ZEMIN_KAT_KATSAYISI,alani_hesapla(en,boy)))


    elif secim=="h":
     print("cıkış yapılıyor ")
    break

else:
    print("hatalı işlem")