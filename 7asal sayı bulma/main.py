("""
*********************

asal sayı bulma şekli şemali

********************

""")
def asal_mı(sayı):
    if(sayı == 1):
        return False
    elif(sayı == 2):
        return True
    else:
        for i in range(2,sayı):
            if(sayı % i == 0):
                return False
        return True
while True:
    sayı = input("sayı:")

    if(sayı == "q"):
        break
    else:
        sayı = int(sayı)

        if(asal_mı(sayı)):
            print(sayı,"asal bir sayıdır")
        else:
            print(sayı,"asal bir sayı değildir")