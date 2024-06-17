from kütüphane import *


print("""*********************


işlemler:

1. kitap göster

2. kitap sorgulama

3. kitap ekle

4. kitap sil

5. baskı yükselt

çıkmak için q ya basın

******************""")


kütüphane = Kütüphane()



while True:
    işlem = input("yapacağınız işlem:")
    if(işlem == "q"):
        print("program sonlandırılıyor...")
        print("yine bekleriz....")
        break
    elif(işlem == "1"):
        pass
    elif (işlem == "2"):
        pass
    elif (işlem == "3"):
        pass
    elif (işlem == "4"):
        pass
    elif (işlem == "5"):
        pass
    else:
        print("geçersiz işlem.")
