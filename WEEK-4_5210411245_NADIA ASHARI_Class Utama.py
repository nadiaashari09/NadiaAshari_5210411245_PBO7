#NADIA ASHARI
#5210411245

class Utama:
  def __init__(self):
    self._a = 2

class Turunan(Utama):
  def __init__(self):
    #Memanggil konstruktor pada kelas Utama
    Utama.__init__(self)
    print("Memanggil variable protected pada class Utama: ",self._a)

    #Modify the protected variable
    self._a = 3
    print("Memanggil variable protected yang dimodifikasi diluas class: ",self._a)

objek1 = Turunan()
objek2 = Utama()

#Memanggil variable protected 
print("Mengakses variable protected dari objek: ", objek1._a)
print("Mengakses variable protected dari objek: ", objek2._a)