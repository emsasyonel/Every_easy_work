class dosya():
    def __init__(self):
        with open("metin.txt","r",encoding = "utf-8") as file:
            dosyaiçeriği = file.read()

            kelimeler = dosyaiçeriği.split()
            self.sadekelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip("")
                i = i.strip(".")
                i = i.strip(",")
                self.sadekelimeler.append(i)

    def tümkelimeler(self):
        kelimelerkümesi = set()
        for i in self.sadekelimeler():
            kelimelerkümesi.add(i)
        print("tüm kelimeler.....")

        for i in kelimelerkümesi:
            print(i)

            print("******************")

dosya = dosya()

dosya.tümkelimeler()