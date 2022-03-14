#NADIA ASHARI
#5210411245
#PBO-7 WEEK 5

#Single Inheritance

#Parent Class
class Hewan:
    def bersuara(self):
        print('Kucing bersuara')

#Child class mewarisi class Hewan
class Kucing(Hewan):
    def suara(self):
        print('meong...meong...meong...')

#Objek
k = Kucing()
k.suara()
k.bersuara()