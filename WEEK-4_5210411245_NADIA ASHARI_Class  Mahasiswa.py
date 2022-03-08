#NADIA ASHARI
#5210411245

class Mahasiswa :
    def __init__ (self, nama, nim, prodi, universitas) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.__universitas = universitas

    def Tampil(self) :
        print(f"{self.nama} adalah mahasiswa {self.nim} prodi {self.prodi} dengan {self.__universitas}")

mahasiswa1 = Mahasiswa("Agung Prayogi", "5210411206", "Teknik Elektro", "Universitas Sumatera Utara")
mahasiswa2 = Mahasiswa("Elvi Syahriani Putri", "5210411201", "Sastra Jepang", "Universitas Darma Persada ")
mahasiswa3 = Mahasiswa("Nadia Ashari", "5210411245", "Informatika", "Universitas Teknologi Yogyakarta")
mahasiswa4 = Mahasiswa("Khalbi Ayub", "5210411203", "Teknik Mesin", "Universitas Sumatera Utara")

kumpulan_mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("\n\tList Mahasiswa\n================================")
for mhs in kumpulan_mahasiswa :     
    mhs.Tampil()
print("\n")