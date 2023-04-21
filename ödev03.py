kelime1 =  str(input("1. Kelimeyi Giriniz:\n-->"))
kelime2 =  str(input("\n2. Kelimeyi giriniz:\n-->"))
kelimeler = []

#Kelimeleri küçült ve listeye ekle
kelime1 = kelime1.lower()
kelimeler.append(kelime1)
kelime2 = kelime2.lower()
kelimeler.append(kelime2)

#Eğer kelime1 ile kelime2 uzunluğu eşitse işlemi başlat
if len(kelime1) == len(kelime2):
    kelime1 = sorted(kelime1)
    kelime2 = sorted(kelime2)
    if kelime1 == kelime2:
        print(kelimeler[0]," ile",kelimeler[1]," anagramdır.")
    else:
        print(kelimeler[0]," ile",kelimeler[1]," anagram değiller.")    

else:
    print(kelimeler[0]," ile",kelimeler[1]," anagram değildirr.")        