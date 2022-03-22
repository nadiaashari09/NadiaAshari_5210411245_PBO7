#NADIA ASHARI
#5210411245
#PBO-7

#Implementasi Overloading Method pada class Computer Part
def rupiah(uang) :
    x = str(uang)
    if len(x) <= 3 :
        return "Rp." + x
    else :
        a = x[:-3]
        b = x[-3:]
        return rupiah(a) + '.' + b

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
        print("\nTampil dari sub class Processor")
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga\t\t: {rupiah(self.harga)}")

class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    #Overload Method
    def Tampil(self, kapasitas) :
        print("\nTampil dari sub class RandomAccessMemory")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {kapasitas}")
        print(f"Harga\t\t: {rupiah(self.harga)}")

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    #Overload Method
    def Tampil(self, kapasitas, rpm) :
        print("\nTampil dari sub class HardDiskSATA")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {kapasitas}")
        print(f"RPM\t\t: {rpm}\nHarga\t\t: {rupiah(self.harga)}")


p = Processor('Intel', 'Core i7 7740X', 4350000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000)
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000)

print("\n\t\t\tOVERLOADING COMPUTER PART")
print("=================================================================================")
p.Tampil()
ram.Tampil("4GB")
hdd.Tampil("500GB", 7200)
print("=================================================================================\n")