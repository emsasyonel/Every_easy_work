print("""

**********************************
kullanıcı girişi
**********************************





""")

sys_kullanıcı_adı = "emre"
sys_parola = "emre123"

kullanıcı_adı = input("kullanıcı adı:")
parola = input("parola:")

if  (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("parola hatalı..")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print ("kullanıcı adı hatalı..")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("kullanıcı adı ve parola hatalı....")
else:
    print("sisteme giriş yapılıyor........")