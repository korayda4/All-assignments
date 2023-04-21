import os

kayıtlılar =[]
def kaydet(kayıtlılar):
    with open("sözlük.txt", "w") as dosya:
        for satir in kayıtlılar:
            dosya.write(f"{satir} \n")

def yukle():
    kayıtlılar = []
    if os.path.exists("sözlük.txt"):
        with open("sözlük.txt", "r") as dosya:
            for satir in dosya:
                satir = satir.strip()
                kayıtlılar.append(satir)
    return kayıtlılar


kayıtlılar = []
kayıtlılar = yukle()
while True:
    
    islem = input("\n İşlem seçiniz:\n 1) Kelime Kontrol\n 2) Yeni Kelime Ekle \n 3) Tüm kelimeleri listele\n -->")

    if islem == "3" or islem.lower() =="tüm kelimeleri listele":
        k = 1
        for i in kayıtlılar:
             print("{}. kelime : {}".format(k,i))
             k += 1
        devam = input("Tekrar işlem yapmak ister misiniz?\n-->")
        if devam.lower() == "evet" or devam.lower() == "e":
            continue
        else:
            break

    if islem == "2" or islem.lower() =="kelime ekle":
        kelime = input("Eklenecek kelimeyi giriniz\n-->")
        if kelime.lower() in kayıtlılar:
            print("Bu kelime kayıtlı")
        if not kelime.lower() in kayıtlılar:
            kayıtlılar.append(kelime)
            kaydet(kayıtlılar)
            print("Başarıyla Kaydedildi")
            devam = input("Tekrar işlem yapmak ister misiniz?\n-->")
            if devam.lower() == "evet" or devam.lower() == "e":
                continue
            else:
                break

    
    if islem == "1" or islem.lower() =="kelime kontrol":
        kelime = input("Aranacak Kelimeyi giriniz\n-->")
        if kelime.lower() in kayıtlılar:
            print("Bu kelime kayıtlı")
            devam = input("Tekrar işlem yapmak ister misiniz?\n-->")
            if devam.lower() == "evet" or devam.lower() == "e":
                continue
            else:
                break
        if not kelime.lower() in kayıtlılar:
            soru =   input("Bu kelime kayıtlı değil! kaydedilsin mi?\n-->")  
            if soru.lower() == "evet" or soru.lower() == "e":
                kayıtlılar.append(kelime)
                kaydet(kayıtlılar)
                print("Başarıyla Kaydedildi")
                devam = input("Tekrar işlem yapmak ister misiniz?\n-->")
                if devam.lower() == "evet" or devam.lower() == "e":
                     continue
                else:
                     break