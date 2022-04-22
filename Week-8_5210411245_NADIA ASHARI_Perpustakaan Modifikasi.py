#NADIAASHARI
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

    def Tampil(self) :
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Pengarang : {self.pengarang}")
        print(f"Jumlah Halaman : {self.jmlhal}")
        print(f"Kategori : {self.subjek}\n")

class Majalah(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, volume, issue):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.volume = volume
        self.issue = issue

    def Tampil(self) :  #Overriding
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Volume : {self.volume}")
        print(f"Issue : {self.issue}")
        print(f"Kategori : {self.subjek}\n")

class DVD(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, aktor, genre):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.aktor = aktor
        self.genre = genre

    def Tampil(self) :  #Overriding
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Aktor : {self.aktor}")
        print(f"Genre : {self.genre}")
        print(f"Kategori : {self.subjek}\n")

#Objek Buku
buku1 = Buku("103", "Pemrograman Python", "Buku Cetak", "Rak No 1", "Dipinjam", "945-884-98-05", "Yogi Syarif", 20, "25x15")
buku2 = Buku("174", "The Pragmatic Programmer", "Buku Cetak", "Rak No 1", "Dpinjam", "978-0135957059", "Andrew Hunt,David Thomas", 100, "18,2 x 25,7")
buku3 = Buku("197", "Think & Grow Rich", "Buku Referensi", "Rak No 1", "Ada", "9786020622279", "Napoleon Hill", 50, "15x23")
buku4 = Buku("176", "Logika Pemograman Python", "Buku Cetak", "Rak No 1", "Ada", "9786230002281", "Abdul Kadir", 170, "14 x 21")

#Objek Majalah
majalah1 = Majalah("209", "Jendela Pendidikan dan Kebudayaan", "Majalah Cetak", "Rak No 2", "Dipinjam", "XVIII", "Pendidikan")
majalah2 = Majalah("299", "Dunia Komputer", "Majalah Cetak", "Rak No 2", "Ada", "VII", "Komputer")
majalah3 = Majalah("277", "Smithsonian", "Majalah Cetak", "Rak No 2", "Dipinjam", "I", "Sains")
majalah4 = Majalah("250", "Tokyo Ghoul", "Majalah Manga", "Rak No 2", "Ada", "IX", "Anime")
majalah5 = Majalah("265", "National Geographic", "Majalah Manga", "Rak No 2", "Ada", "I", "Sejarah")

#Objek DVD
dvd1 = DVD("304", "Harry Potter and The Sorcerers Stone", "softcopy", "Rak No 3", "Ada", "Daniel Radcliffe", "Fiksi")
dvd2 = DVD("345", "Harry Potter and the Prisoner of Azkaban", "softcopy", "Rak No 3", "Ada", "Daniel Radcliffe", "Fiksi")
dvd3 = DVD("325", "Enola Holmes", "softcopy", "Rak No 3", "Ada", "Millie Bobby Brown", "Petualangan")
dvd4 = DVD("309", "Spirited Away", "softcopy", "Rak No 3", "Ada", "Chihiro Ogino", "Anime")

buku = [buku1, buku2, buku3, buku4]
majalah = [majalah1, majalah2, majalah3, majalah4, majalah5]
dvd = [dvd1, dvd2, dvd3, dvd4]

while True :
    print("=======================\n    SEARCH ITEM \n=======================")
    print("1. BUKU ")
    print("2. MAJALAH")
    print("3. DVD")
    print("0. selesai")
    menu = input("Pilihan Menu : ")

    if menu == '1' :
        print("\nMENU BUKU\n===============\n1. Tampil Buku")
        print("2. Cari Buku")
        pilihan = input("Pilihan : ")
        buku = [buku1, buku2, buku3, buku4]

        if pilihan == '1' :
            print("\n==============================================")
            for buku in buku :
                buku.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode Buku\t: ")
            for x in buku :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '2' :
        print("\nMENU MAJALAH\n===============\n1. Tampil Data Majalah")
        print("2. Cari Majalah")
        pilihan = input("Pilihan : ")
        majalah = [majalah1, majalah2, majalah3, majalah4, majalah5]

        if pilihan == '1' :
            print("\n==============================================")
            for majalah in majalah :
                majalah.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode Majalah\t: ")
            for x in majalah :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '3' :
        print("\nMENU DVD\n===============\n1. Tampil Data DVD")
        print("2. Cari DVD")
        pilihan = input("Pilihan : ")
        dvd = [dvd1, dvd2, dvd3, dvd4]

        if pilihan == '1' :
            print("\n==============================================")
            for dvd in dvd :
                dvd.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode DVD\t: ")
            for x in dvd :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '0' :
        print("TERIMA KASIH :)\n")
        break

    else :
        print("\nPilihan Tidak Ada Menu\n")
    input("\nEnter Untuk Melanjutkan......")

#NADIA ASHARI
#5210411245