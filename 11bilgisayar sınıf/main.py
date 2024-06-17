import time
class bilgisayar():

    def __init__(self,bilgisayar_durum = "kapalı",bilgisayar_ses = 0, uygulama_listesi = ["desktop"],uygulama = "lol"):
        self.bilgisayar_durum = bilgisayar_durum
        self.bilgisayar_ses = bilgisayar_ses
        self.uygulama_listesi = uygulama_listesi
        self.uygulama = uygulama
    def pc_aç(self):
        if(self.bilgisayar_durum == "açık"):
            print("bilgisayar zaten açık.")
        else:
            print("bilgisayar açılıyor.")
            self.bilgisayar_durum == "açık"
    def pc_kapat(self):
        if(self.bilgisayar_durum == "kapalı"):
            print("tevizyon zaten kapalı.")
        else:
            print("televizyon kapanıyor.")
            self.bilgisayar_durum == "kapalı"
    def bilgisayar_ses(self):
        while True:
            cevap = input("sesi azalt:  '<'\nsesi arttır:  '>'\nçıkış = çıkış")
            if (cevap == "<"):
                if(self.bilgisayar_ses != 0):
                    self.bilgisayar_ses -= 1
                    print("ses",self.bilgisayar_ses)
            elif(cevap == ">"):
                if(self.bilgisayar_ses != 31):
                    self.bilgisayar_ses += 1
                    print("ses",self.bilgisayar_ses)
            else:
                print("ses güncellendi:",self.bilgisayar_ses)
                break
    def uygulama_ekle(self,uygulama_ismi):
        print("uygulama ekleniyor.")
        self.uygulama_listesi.append(uygulama_ismi)
        print("uygulama eklendi.")
    def oyun_ekle(self,oyun_ekle):
        print("uygulama ekleniyor.")
        self.uygulama.append(oyun_ekle)
        print("oyun eklendi.")
        
