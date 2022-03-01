#NADIA ASHARI
#5210411245

class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

mahasiswa1 = Mahasiswa("Agung Prayogi", "5210411206", "Teknik Elektro")
mahasiswa2 = Mahasiswa("Elvi Syahriani Putri", "5210411201", "Sastra Jepang")
mahasiswa3 = Mahasiswa("Nadia Ashari", "5210411245", "Informatika")
mahasiswa4 = Mahasiswa("Khalbi Ayub", "5210411203", "Teknik Mesin")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("List Mahasiswa")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")