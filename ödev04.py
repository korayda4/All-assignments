msg = "Bir şifre belirleyin\n-->"
while True:
    sifre = input(msg)
    if len(sifre) < 8:
        print("Şifreniz en az 8 karakter olmalıdır. Lütfen tekrar deneyin.")
        msg = "Bir şifre belirleyin(En az 8 karakter içermelidir)\n-->"
        continue
    if not any(kntrl.isdigit() for kntrl in sifre):
        print("Şifreniz en az 1 rakam içermelidir. Lütfen tekrar deneyin.")
        msg = "Bir şifre belirleyin(Birtane rakam bulundurun)\n-->"
        continue
    if not any(kntrl.isalpha() for kntrl in sifre):
        print("Şifreniz en az 1 harf içermelidir. Lütfen tekrar deneyin.")
        msg = "Bir şifre belirleyin(Birtane harf bulundurun)\n-->"
        continue
    if not any  (kntrl.isupper() for kntrl in sifre):      
        print("En az birtane büyük harf içermelidir.Lütfen tekrar deneyin.")
        msg = "Bir şifre belirleyin(Birtane büyük harf bulundurun)\n-->"
        continue
    else:
        print("Şifre Oluşturuldu!")
        
        break

    
    