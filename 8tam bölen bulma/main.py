def tambolen(sayı):
    tam_bolenler = []

    for i in range(1,sayı + 1):
        if (sayı % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler
while True:
    sayı = input("sayı:")
    if (sayı == "q"):
        print("çıkılıyor")
        break
    else:
        sayı = int(sayı)
        print("tam bölenler",tambolen(sayı))