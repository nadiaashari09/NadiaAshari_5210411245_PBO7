#NADIA ASHARI
#5210411245

class Menu :
    def __init__(self, nama, deskripsi, harga, menu_tambahan, harga_tambahan) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__menu_tambahan = menu_tambahan
        self.__harga_tambahan = harga_tambahan

minuman1 = Menu("Americano", "Kopi espresso tanpa gula", 20000, "ice", 1000)
minuman2 = Menu("Cappuccino", "Kopi espresso dengan susu", 25000, "ice", 1000)
minuman3 = Menu("Mochaccino", "Kopi espresso dengan susu, chocolate, dan caramel", 25000, "ice", 1000)
minuman4 = Menu("Affogato", "Kopi espresso dengan ice cream vanilla", 23000, "ice", 1000)

makanan1 = Menu("Croissant Butter", "Roti Croissant dengan mentega", 18000, "Chocolate Sauce", 3000)
makanan2 = Menu("Chocolate Banana", "Pisang bakar dengan coklat", 25000, "Ice Cream", 5000)
makanan3 = Menu("Cinnamon Roll", "Roti gulung dengan rasa cinnamon", 20000, "Vanilla Sauce", 3000)
makanan4 = Menu("Chocolate Cupcake", "Cupcake dengan rasa coklat dan lelehan coklat didalamnya", 20000, "Ice Cream", 5000)

makanan = [makanan1, makanan2, makanan3, makanan4]
minuman = [minuman1, minuman2, minuman3, minuman4]

print("Daftar Menu Makanan")
for makan in makanan :
    teks = '{} harga Rp {}, {}. Dengan menambah Rp {} anda bisa mendapatkan Extra {}.'. format(makan.nama, makan.harga, makan.deskripsi, makan._Menu__harga_tambahan, makan._Menu__menu_tambahan)
    print(teks)
print("\nDaftar Menu Minuman")
for minum in minuman :
    teks = '{} harga Rp {}, {}. Dengan menambah Rp {} anda bisa mendapatkan Topping tambahan {}.'. format(minum.nama, minum.harga, minum.deskripsi, minum._Menu__harga_tambahan, minum._Menu__menu_tambahan)
    print(teks)
print("\n")