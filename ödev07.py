print("İki seçenekli oyuna hoşgeldin! seçenekleri seçerek hikayeyi kendin oluştur!")
while True:
    soru1 = input("Sabah uyandın saat 11.46 fakat güneş doğmamış! ilk olarak ne yapardın?\n1) Hemen internet üzerinden bir araştırma yap \n2) Hışarı çıkıp etrafı kontrol et\n-->")
       
    if soru1 == "1":
      soru2 = input("İnternet üzerinden yaptığın araştırma sonucu küresel bir sorun olduğunu ve dünyanın hızla sıcaklık kaybettiğini öğrendin! ne yapardın?\n1)Beni sıcak tutacak giysi seçer ve sığınak gibi yer ara \n2)Aile ve arkadaşlarına durumu sor\n-->")
      if soru2 == "2":
         soru3 = input("Ailene veya arkadaşlarına ulaşamadın! ne yapardın? \n1)Eve geri döner ve haberlerden talimat beklerim \n2)Dışarıda bir askeri araç veya onun gibi bir şey beklerim\n-->")
         if soru3 == "2":
            soru4 = input("Dışarıda hiç kimse yok! hava sıcaklığı 5 dereceye kadar düştü! ne yapardın?\n1)Uyduyu düzeltmek için çatıya çıkarım\n2)karakol veya başka bir resmi yer ararım\n-->")
            if soru4 == "2":
               soru5 = input("karakol veya benzer bir şey bulamadın ve hava çok soğudu! ne yapardın? \n1)Ölmeyi beklerim\n2)-\n-->")
               if soru5 == "1" or soru5 == "2":
                  tekrar = input("Öldün tekrar oynamak ister misin?(E/H)\n-->")
                  if tekrar.lower == "e":
                     continue
                  else:
                     break

               
            if soru4 == "1":
                soru5 = input("Uyduyu düzeltmek için çatıya çıktığın sırada çıktığın kapı sıkıştı ve geri dönemiyorsun! hava -10 derece oldu! ne yapardın? \n1)Kapıyı açmaya zorlar veya kırmaya çalışırdım\n2)İlk olarak uyduyu düzeltirdim ve yardım aramaya çalışırdım\n-->")
                if soru5 == "2":
                   print("Uyduyu düzelttin fakat yardım bulamadın ve donarak öldün! Tekrar Oynamak ister misin?(E/H)\n-->")
                   tekrar = input()
                   if tekrar.lower == "e":
                      continue
                   else:
                      break
                    
                   
                if soru5 == "1":
                    print("Kapıyı açamadın ve omuz atarak kırmayı denedin. 3. deneyişte kapı kırıldı fakat o ivmeyle merdivenlerden yuvarlanıp kafanı sert şekilde vurdun ve öldün\n-->")
                    tekrar = input("Oyunu Kaybettin! Tekrar oynamak ister misin?(E/H)\n-->")
                    if tekrar.lower() == "e":
                       continue
                    else:
                       break

         if soru3 == "1":
            soru4 = input("Eve geldin fakat uydu çekmiyor! hava sıcaklığı 5 dereceye kadar düştü! ne yapardın?\n1)Uyduyu düzeltmek için çatıya çıkarım\n2)Doğalgazı sonuna kadar açarım\n-->")
            if soru4 == "2":
               tekrar = input("Doğalgaz patladı ve öldün! Tekrar oynamak ister misin?(E/H)\n-->")
               if tekrar.lower() == "e":
                    continue
               else:
                    break
            if soru4 == "1":
                soru5 = input("Uyduyu düzeltmek için çatıya çıktığın sırada çıktığın kapı sıkıştı ve geri dönemiyorsun! hava -10 derece oldu! ne yapardın? \n1)Kapıyı açmaya zorlar veya kırmaya çalışırdım\n2)İlk olarak uyduyu düzeltirdim ve yardım aramaya çalışırdım\n-->")
                if soru5 == "2":
                   tekrar = input("Yardım bulamadın ve donarak öldün! Tekrar oynamak ister misin?(E/H)\n-->")
                   if tekrar.lower() == "e":
                       continue
                   else:
                       break
                if soru5 == "1":
                    print("Kapıyı açamadın ve omuz atarak kırmayı denedin. 3. deneyişte kapı kırıldı fakat o ivmeyle merdivenlerden yuvarlanıp kafanı sert şekilde vurdun ve öldün\n-->")
                    tekrar = input("Oyunu Kaybettin! Tekrar oynamak ister misin?(E/H)\n-->")
                    if tekrar.lower() == "e":
                       continue
                    else:
                       break
         
      if soru2 == "1":
        soru3 = input("Giysilerini aldın ve sığınak arayışına geçtin fakat türkiyede sığınak yok! ne yapardın? \n1)Eve geri döner ve haberlerden talimat beklerim \n2)Dışarıda bir askeri araç veya onun gibi bir şey beklerim\n-->")
        if soru3 == "2":
           tekrar = input("Hiç bir askeri araç gelmedi donarak öldün! Tekrar oynamak ister misin?(E/H)\n-->")
           if tekrar.lower() == "e":
              continue
           else:
              break
           
        if soru3 == "1":
            soru4 = input("Eve geldin fakat uydu çekmiyor! hava sıcaklığı 5 dereceye kadar düştü! ne yapardın?\n1)Uyduyu düzeltmek için çatıya çıkarım\n2)Doğalgazı sonuna kadar açarım\n-->")
            if soru4 == "1":
                soru5 = input("Uyduyu düzeltmek için çatıya çıktığın sırada çıktığın kapı sıkıştı ve geri dönemiyorsun! hava -10 derece oldu! ne yapardın? \n1)Kapıyı açmaya zorlar veya kırmaya çalışırdım\n2)İlk olarak uyduyu düzeltirdim ve yardım aramaya çalışırdım\n-->")
                if soru5 == "1":
                    print("Kapıyı açamadın ve omuz atarak kırmayı denedin. 3. deneyişte kapı kırıldı fakat o ivmeyle merdivenlerden yuvarlanıp kafanı sert şekilde vurdun ve öldün\n-->")
                    tekrar = input("Oyunu Kaybettin! Tekrar oynamak ister misin?(E/H)\n-->")
                    if tekrar.lower() == "e":
                       continue
                    else:
                       break
         
    if soru1 == "2":
        soru2 = input("Dışarı kısa kol T-Shirt ile çıktın ve anahtarı almayı unuttun fakat hava çok soğuk! ne yapardın?\n1)Polisten veya vatandaştan yardım iste\n2)Kapıyı açmaya veya kırmaya çalış\n-->")
        if soru2 == "2":
           tekrar = input("Kapıyı kıramadın ve donarak öldün! Tekrar oynamak ister misin?\n-->")
           if tekrar.lower() == "e":
              continue
           else:
              break
           
        if soru2 == "1":
            soru3 = input("Kimse dışarı çıkmadı ve sana yardım etmedi! ne yapardın?\n1)Eve girmeye çalışır veya kapıyı kırmaya çalışırdım \n2)Dışarıda bir askeri araç veya onun gibi bir şey beklerim\n-->")
            if soru3 == "2":
               tekrar = input("Hiç bir askeri araç gelmedi ve donarak öldün! Tekrar oynamak ister misin?(E/H)\n-->")
               if tekrar.loer() == "e":
                  continue
               else:
                  break
               
            if soru3 == "1":
                soru4 = input("kapıyı açamadın! hava sıcaklığı 5 dereceye kadar düştü! ne yapardın?\n1)Ölmeyi beklerdim\n2)teker teker komşuları gezerdim\n-->")
                if soru4 == "2":
                   tekrar = input("Kimse seni içeri almadı ve donarak öldün! Tekrar oynamak ister misin?(E/H)\n-->")
                   if tekrar.lower() == "e":
                      continue
                   else:
                      break
                   
                if soru4 == "1":
                   devam = input("Donarak öldün! Tekrar oynamak ister misin?(E/H)\n-->")
                   if devam.lower() == "e":
                      continue
                   else:
                      break