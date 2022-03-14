#NADIA ASHARI
#5210411245
#PBO-7 WEEK 5

#Multilevel Inheritance Computer Part

class ComputerPart:
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampil(self) :
        print(f"{self.nama} produk dari {self.pabrikan} dijual dengan harga {rupiah(self.harga)}")

class RandomAccessMemory(Processor) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampil(self) :
        print(f"{self.nama} produk dari {self.pabrikan} dijual dengan harga {rupiah(self.harga)}")

class HardDiskSATA(RandomAccessMemory) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampil(self) :
        print(f"{self.nama} produk dari {self.pabrikan} dijual dengan harga {rupiah(self.harga)}")

def rupiah(uang) :
    x = str(uang)
    if len(x) <= 3 :
        return "Rp." + x
    else :
        a = x[:-3]
        b = x[-3:]
        return rupiah(a) + '.' + b

p = Processor('Intel', 'Core i7 7740X', 4350000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000)
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000)

parts = [p, ram, hdd]
print("\n\t\t\tMULTILEVEL INHERITANCE COMPUTER PART")
print("=================================================================================")
for part in parts :
    part.Tampil()
print("=================================================================================\n")

#PBO-7 WEEK 5
#5210411245
#NADIA ASHARI