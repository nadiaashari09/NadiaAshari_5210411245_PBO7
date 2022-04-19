#NADIASHARI
#5210411245

class Perpustakaan :
    def __init__(self, kode, judul, subjek, lokasi, info) :
        self.kode = kode
        self.judul = judul
        self.subjek = subjek
        self.lokasi = lokasi
        self.info = info

class Buku(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, isbn, pengarang, jmlhal, ukuran):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal
        self.ukuran = ukuran

class Majalah(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, volume, issue):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.volume = volume
        self.issue = issue

class DVD(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, aktor, genre):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.aktor = aktor
        self.genre = genre

buku = Buku("174", "The Pragmatic Programmer", "Buku Cetak", "Rak No 1", "Dpinjam", "978-0135957059", "Andrew Hunt,David Thomas", 100, "18,2 x 25,7")
majalah = Majalah("250", "Tokyo Ghoul", "Majalah Manga", "Rak No 2", "Ada", "IX", "Anime")
dvd = DVD("325", "Enola Holmes", "softcopy", "Rak No 3", "Ada", "Millie Bobby Brown", "Petualangan")
objects = [buku, majalah, dvd]

for object in objects :
    print(f"Judul : {object.judul}")
    print(f"Kategori : {object.subjek}")
    print(f"Lokasi : {object.lokasi}")
    print(f"Status : {object.info}\n")

#5210411245
#NADIAASHARI