#NADIA ASHARI
#5210411245

#Private dan Public
class Pegawai:
    __nama=""
    __alamat=""
    __gaji=0
    
    def __init__(self,nama,alamat):
        self.__nama=nama
        self.__alamat=alamat
        
    def __hitungGaji(self):
        upahLembur=20000
        gajiPokok=2000000
        jumLembur=int(input("total jam lembur: "))
        self.__gaji=(upahLembur*jumLembur)+gajiPokok
        
    def tampilDetail(self):
        print("\n--Menghitung dan Menampilkan Detail Gaji Pegawai--")
        print("Nama: ", self.__nama)
        print("Alamat: ", self.__alamat)
        self.__hitungGaji()
        print("Total Gaji: ", self.__gaji)
        
#membuat objek pegawai
pgw1=Pegawai("Mikasa Ackerman", "Wall Rose")
pgw1.tampilDetail()

pgw2=Pegawai("Saya Kisaragi", "prefektur Nagano")
pgw2.tampilDetail()