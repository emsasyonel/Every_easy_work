def nothesapla(satır):

    satır = satır[:-1]
    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    sonnot = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (sonnot >= 90):
        harf = "AA"
    elif(sonnot >= 85):
        harf = "BA"
    elif (sonnot >= 80):
        harf = "BB"
    elif (sonnot >= 75):
        harf = "CB"
    elif (sonnot >= 70):
        harf = "CC"
    elif (sonnot >= 65):
        harf = "DC"
    elif (sonnot >= 60):
        harf = "DD"
    elif (sonnot >= 55):
        harf = "FD"
    else:
        harf = "FF"
    return isim +"..............>" + harf + "\n"



with open("dosya.txt", "r", encoding="utf-8") as file:
    ekleneceklerlistesi = []

    for i in file:
        ekleneceklerlistesi.append(nothesapla(i))

    with open("notlar.txt","w",encoding = "utf-8") as file2:
        for i in ekleneceklerlistesi:
            file2.write(i)
