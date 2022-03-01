#NADIA ASHARI
#5210411245

class Menu :
    def __init__(self, nama, deskripsi, harga) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

minuman1 = Menu("Americano", "Kopi espresso tanpa gula", 20000)
minuman2 = Menu("Cappuccino", "Kopi espresso dengan susu", 25000)
minuman3 = Menu("Mochaccino", "Kopi espresso dengan susu, chocolate, dan caramel", 25000)
minuman4 = Menu("Affogato", "Kopi espresso dengan ice cream vanilla", 23000)

makanan1 = Menu("Croissant Butter", "Roti Croissant dengan mentega", 18000)
makanan2 = Menu("Chocolate Banana", "Pisang bakar dengan coklat", 25000)
makanan3 = Menu("Cinnamon Roll", "Roti gulung dengan rasa cinnamon", 20000)
makanan4 = Menu("Chocolate Cupcake", "Cupcake dengan rasa coklat dan lelehan coklat didalamnya", 20000)

makanan = [makanan1, makanan2, makanan3, makanan4]
minuman = [minuman1, minuman2, minuman3, minuman4]

print("Daftar Menu Makanan")
for makan in makanan :
    teks = '{} harga Rp {}, {}'. format(makan.nama, makan.harga, makan.deskripsi)
    print(teks)
print("\nDaftar Menu Minuman")
for minum in minuman :
    teks = '{} harga Rp {}, {}'. format(minum.nama, minum.harga, minum.deskripsi)
    print(teks)
print("\n")