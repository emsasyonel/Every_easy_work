def ekstra(fonk):
    def wrapper(sayılar):
        çiftler_toplamı = 0
        çift_sayılar = 0
        tekler_toplamı = 0
        tek_sayılar = 0

        for sayı in sayılar:
            if(sayı % 2 == 0):
                çiftler_toplamı += sayı
                çift_sayılar += 1
            else:
                tekler_toplamı += sayı
                tek_sayılar += 1
        print("teklerin ortalaması:",tekler_toplamı / tek_sayılar)
        print("çiflerin ortalaması:",çiftler_toplamı / çift_sayılar)

        fonk(sayılar)
    return wrapper


@ekstra
def ortalama_bul(sayılar):
    toplam = 0

    for sayı in sayılar:
        toplam += sayı
        print("genel ortalama:",toplam/len(sayılar))

ortalama_bul([1,2,3,4,34,35,36,80,45,45555,7000000])