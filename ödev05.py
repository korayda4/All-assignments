sorular = ["2+5 Kaçtır?", "Kaç yaşındayım?", "İsmim ne?", "Eğitim kaç ay?", "Hangi Eğitimi alıyoruz?", "Sınıf kaç kişilik?", "Türkiyede kaç il var?", "Bilgisayarımın markası ne?", "Öğretmenin adı ne?", "Hangi Üniversitedeyiz?"]
cevaplar = ["a","b","a","c","b","b","d","a","d","d"]
abcd = ["A)7\nB)4\nC)9\nD)11","A)23\nB)18\nC)21\nD)11","A)Koray\nB)Ecren\nC)Bekir\nD)Orhan","A)7\nB)5\nC)6\nD)11","A)Psikoloji\nB)Genişletilmiş Yazılım Uzmanlığı\nC)Muhasebe\nD)Diş hekimliği","A)55\nB)30\nC)20\nD)45","A)41\nB)156\nC)83\nD)81","A)Casper\nB)Asus\nC)MSİ\nD)Lenovo","A)Musa\nB)Ercan\nC)Mehmet\nD)Orhan","A)OMÜ\nB)İTÜ\nC)İÜ\nD)NÜ"]
dogru, yanlis = 0, 0

for i in range(10):
    print(f"Soru {i+1}: {sorular[i]}")
    print(abcd[i])
    cevap = input("Cevap: ").lower()

    if cevaplar[i] == cevap:
        print("\nCevap Doğru!\n")
        dogru += 1
    else:
        yanlis += 1
        print(f"Yanlış cevap verdiniz. Doğru cevap: {cevaplar[i]}\n")

print(f"Toplam {dogru+yanlis} sorunun {dogru} tanesini doğru cevapladınız {yanlis} Tanesini yanlış cevapladınız")

