#NADIA ASHARI
#5210411245
#PBO-7

#Polymorphism dengan fungsi
#Simple example using Len function

print(len("Polymorphism"))
print(len([0,1,2,3]))

'''
Menggunakan Fungsi len
Output :
12 (Tipe Data Saring)
4 (Tipe Data List)
'''

#using class
class jerman:
    def ibukota(self):
        print("Berlin adalah ibukota negara Jerman")

class jepang:
    def ibukota(self):
        print("Tokyo adalah ibukota negara Jepang")

negara1 = jerman()
negara2 = jepang()

for country in (negara1, negara2):
    country.ibukota()
