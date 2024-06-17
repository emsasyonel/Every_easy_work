print("""

hesap makinesi programı

işlemler : 

1. toplama işlemi
2. çıkarma işlemi
3. çarpma işlemi
4. bölme işlemi




""")


a = int(input("bir sayı giriniz:"))
b = int(input("bir sayı giriniz:"))

işlem = input("işlemi giriniz:")

if işlem == "1":
    print("{} ile {} in toplamı {} dir.".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} in farkı {} dir.".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {} in çarpımı {} dir.".format(a,b,a*b))
elif işlem == "4":
    print("{} ile {} in bölümü {} dir.".format(a,b,a/b))
else:
    print("geçersiz işlem!..")