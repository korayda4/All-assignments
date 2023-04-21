sayi = input("Kaç sayı girmek istiyorsunuz?:\n-->")
sayilist = []
toplam = 0

#değerleri iste ve toplam değişkeninde topla
for i in range(1,int(sayi)+1):
    sayilist.append(input(str(i)+". sayıyı girin:\n-->"))
    toplam = toplam+int(sayilist[int(i)-1])

#işlemler
sayilist.sort(reverse=False)
print("\nSayıların Toplamı:\n-->",toplam)
print("\nSayıların Ortalaması:\n-->",toplam/int(sayi))
print("\nGirilen Değerler:\n-->",sayilist)