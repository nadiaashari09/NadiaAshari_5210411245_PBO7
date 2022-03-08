#NADIA ASHARI
#5210411245

class Buku :
    def __init__(self, judul, pengarang, tahun_terbit, jmlh_halaman) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__jmlh_halaman = jmlh_halaman

    def Tampil(self):
        print(f"Buku {self.judul} karangan {self.pengarang} pertama kali diterbitkan tahun {self.tahun_terbit}")
        print(f"Buku {self.judul} jumlah halamannya adalah {self.__jmlh_halaman}\n")

buku1 = Buku("Jika Kita Tak Pernah Jadi Apa-apa", "Alvi Syahrin", 2020, 248)
buku2 = Buku("Think & Grow Rich", "Napoleon Hill", 1937, 324 )
buku3 = Buku("Insecurity Is My Middle Name", "Alvi Syahrin", 2021, 264)

kumpulan_buku = [buku1, buku2, buku3]
print("\n\tList Buku\n================================")
for buku in kumpulan_buku :     
     buku.Tampil()
print("\n")