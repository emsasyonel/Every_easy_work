import random
import time

print("""

tahmin oyunu

1 ile 40 arasındaa sayıyı tahmin edin
""")

rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7
while True:
    tahmin = int(input("tahmininiz :"))

    if(tahmin < rastgele_sayı):
        print("bilgiler sorgulanıyor..")
        time.sleep(1)


        print("daha yüksek bir sayı giriniz..")

        tahmin_hakkı -= 1
    elif(tahmin > rastgele_sayı):
        print("bilgiler sorgulanıyor...")

        time.sleep(2)

        print("daha düşük bir sayı giriniz..")

        tahmin_hakkı -= 1
    else:
        print("bilgiler sorgulanıyor...")
        time.sleep(1)
        print("tahmininiz doğru.")
        print("tebrikler sayınız:",rastgele_sayı)
        break
    if (tahmin_hakkı == 0):
        print("tahmin hakkınız bitti. Rastgele sayı :",rastgele_sayı)
        break
