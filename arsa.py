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

print("Lutfen arsanin konumunu secin:")
print("1 - Deniz kenari")
print("2 - Sehir merkezi")
print("3 - Kirsal")
bolge_secimi = input("Seç (1/2/3): ")

if bolge_secimi == "1":
    bolge_katsayisi = DENIZ_KENARI
elif bolge_secimi == "2":
    bolge_katsayisi = SEHIR_MERKEZI
elif bolge_secimi == "3":
    bolge_katsayisi = KIRSAL

print("Arsa seklini sec:")
print("1 - Dikdortgen")
print("2 - Cember")
sekil_secimi = input("Sec (1/2): ")

if sekil_secimi == "1":
    en = float(input("Dikdortgenin eni: "))
    boy = float(input("Dikdortgenin boyu: "))
    arsa_cevresi = arsa_cevresi("dikdortgen", en=en, boy=boy)
elif sekil_secimi == "2":
    yaricap = float(input("Cemberin yaricapi: "))
    arsa_cevresi = arsa_cevresi("cember", yaricap=yaricap)

arsa_fiyati = arsa_fiyati_hesapla(bolge_katsayisi, arsa_cevresi)

print(f"Arsanin fiyati: {arsa_fiyati} TL")
