#NADIA ASHARI
#5210411245
#PBO-7

class Segiempat():
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitungLuas(self):   #Method Overriding
        print("Luas Segiempat= ", self.panjang * self.lebar, "m^2")

class Bujursangkar(Segiempat):
    def __init__(self,sisi):
        self.side = sisi
        Segiempat.__init__(self, sisi, sisi)

    def hitungLuas(self):   #Method Overriding
        print("Luas Bujur Sangkar= ", self.side * self.side, "m^2")

b = Bujursangkar(4)
s = Segiempat(2,4)
b.hitungLuas()
s.hitungLuas()