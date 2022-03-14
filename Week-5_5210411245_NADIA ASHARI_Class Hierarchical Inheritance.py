#NADIA ASHARI
#5210411245
#PBO-7 WEEK 5

#Hierarchical Inheritance

class Mahasiswa() :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim

class Siswa1(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim

    def detSiswa1(self) :
        print(self.nama, "Alamat : Wall Rose")

class Siswa2(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim

    def detSiswa2(self) :
        print(self.nama, "Jurusan : Informatika")

mahasiswa1 = Siswa1("Mikasa", 135105)
mahasiswa2 = Siswa2("Nezuko", 135117)

print(mahasiswa1.nim)
mahasiswa1.detSiswa1()
print(mahasiswa2.nim)
mahasiswa2.detSiswa2()