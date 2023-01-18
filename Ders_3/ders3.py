"""
def polinDRAM(*dram):
    toplam = 0
    for sayi in dram:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam


print(polinDRAM(10, 101, 55, 40, 9009))
"""




"""
class sinif:
    pass

nesne = sinif()

print(type(nesne))
"""


"""
class sinif:
    a = 0
    b = "ads"
    c = [1, 3, 5]

nesne = sinif()
print(nesne.a)
nesne.a = 999
print(nesne.a)
"""


"""
class sinif:
    a = 5
    b = "ads"
    c = [1, 3, 5]

    def yazdir(self):
        d = 100
        print(d, self.a)

    def yazdir2(self, t):
        self.yazdir()
        print(t)


nesne = sinif()
nesne.yazdir()
nesne.yazdir2("gfdgfd")
"""




"""
class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a

    def __del__(self):
        print("beni siliyorlar...")

nesne = sinif("Metin")
del nesne
"""

"""
class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a

    def __str__(self):
        return "Yazdırılan : " + self.metin

nesne = sinif("Civa")
print(nesne)
"""



"""
x = "asd"
try:
    y = 5 + x
except:
    print("'int' and 'str'")
"""



from termcolor2 import c

print(c("hello").red.on_white.blink.underline.dark)

