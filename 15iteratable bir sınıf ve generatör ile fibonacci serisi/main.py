class kuvvet3():
    def __init__(self,max = 0):
        self.max = max
        self.kuvvet = 0
    def __iter__(self):
        return self

    def __next__(self):
        if(self.kuvvet <= self.max):
            sonuç = 3 ** self.kuvvet
            self.kuvvet += 1
            return sonuç

        else:
            self.kuvvet = 0
            raise StopIteration
kuvvet = kuvvet3(6)

for i in kuvvet:
    print(i)
for j in kuvvet:
    print(j)


