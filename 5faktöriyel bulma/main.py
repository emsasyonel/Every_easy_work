print("""*******************


faktöriyel bulma

çıkmak için "çıkış" a basın
***************************""")

while True:
    sayı = input("sayı:")

    if(sayı == "çıkış"):
        print("kapanıyor..")
        break

    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2,sayı+1):
            faktoriyel *= i
        print("faktoriyel",faktoriyel)