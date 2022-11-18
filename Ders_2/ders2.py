liste=[]
for i in range(0,5):
    liste.append(eval(input()))

def siralama_fonk(a):
    return a*a-20

liste.sort(key=siralama_fonk)
print(liste)

a=5
c=4
d=-5
if a>c:
    print("a c den büyüktür.")
if d<0:
    print("d 0 dddan küçüktür.")
if d>0: print("asdfaf");print("ddajs");d=5


e=5
if e>5:
    print("e 5ten büyüktür.")
elif e==5:
    print("e 5e eşittir.")
else:
    print("e 5 ten küçüktür.")


a=5
b=4
print("a ile b farkli") if a != b else print("a ile b ayni")



a=5
c=10
b=-4
if a < 10 or c < 10:
    print("a ya da c 10 dan küçük.")
if a == 5 and  c == 10:
    print("a 5e eşit ve c 10a eşit")


a=5
c=10
if a<5:
    if c>10:
        print("merhaba dünya")



a=5
while a<15:
    print(a)
    if a==10:
        continue
    if a==12:
        break
    print(a)

else:
    print("a artık 15 ya da daha büyük")


for i in range(0,10):
    print(i)
for i in range(0,10,2):
    print(i)
for i in range('a','b'):
    print(i)


liste=["as",True,1.9,5,["asdda","sddf","assert"]]
for i in liste:
    print(i)
for i in liste[4]:
    print(i)
for i in range(0,3):
    print(i)
else:
    print("for bitti.")
for i, eleman in enumarate(liste):
    print(i+1,".eleman : ",eleman , sep="")
def yazdir():
    print("yazıyorum")

yazdir()


def topla(a,b)
    return a+b
print(topla(3,5))

def topLA_ne_varsa_git(*a):
    toplam=0
    for deger in a:
        toplam+=a
    return toplam

print(topLA_ne_varsa_git(3,5,9,15.2,36))


def(*toplanacak,fazladan=0):
    toplam=0
    for deger in toplanacak:
        toplam+=deger+fazladan
    return toplam

print(topLA_ne_varsa_git(3,5,9,15.2,36,fazladan=2),file="a.txt")


def birim_islem(**birim):
    print("Birimin tipi: ",type(birim))
    print("Birim adı: "+birim["ad"])
    print("Birim tipi: "+birim["tip"])
    print("Birim yılı: ",birim["yil"])




lambda_fonksiyonu=lambda a:a+10
print(lambda_fonksiyonu(5))


"""BUNUN KULLANILACAĞI BİR SINAV SORUSU!!!!!!!!!!"""

def benimfonk(n):
    return lambda a:a*n

katini_al=benimfonk(2)
print(katini_al(5))

katini_al=benimfonk(5)
print(katini_al(5))
