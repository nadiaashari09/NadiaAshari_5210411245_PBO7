#NADIA ASHARI
#5210411245

class Buku :
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku("Jika Kita Tak Pernah Jadi Apa-apa", "Alvi Syahrin", 2020)
buku2 = Buku("Think & Grow Rich", "Napoleon Hill", 1937)
buku3 = Buku("Insecurity Is My Middle Name", "Alvi Syahrin", 2021)

bukus = [buku1, buku2, buku3]
print("List Buku")
for buku in bukus :
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print("\n")