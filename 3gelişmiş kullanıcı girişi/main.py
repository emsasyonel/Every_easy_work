print("""
****************************
kullanıcı girişi programı
""")

sys_kullanıcı_adı = "emre"

sys_parola = "emre123"

giriş_hakkı = 3


while True:
    kullanıcı_adı = input("kullanıcı adı:")
    parola = input("parola:")
    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("kullanıcı adı hatalı...")
        giriş_hakkı -= 1
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("parola hatalı..")
        giriş_hakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("kullanıcı adı ve parola hatalı...")
        giriş_hakkı -= 1
    else:
        print("sisteme başarıyla giriş yapıldı...")
        break
    if (giriş_hakkı == 0):
        print("giriş hakkınız biti ! yeniden başlatınız...")
        break
