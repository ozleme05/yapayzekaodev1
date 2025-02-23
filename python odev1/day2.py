from human import Human
import matematik as math

math.bol(20,10)

faiz = 1.59
vade = "36"
krediAdi = "ihtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade) + 12)
# print(int(krediAdi))
faiz=str(faiz)
print(type(faiz))

# iki noktadan sonra boşluk önemli 
# print(int(vade) + 12)yaparsak int olur
vade = 12 #int(input("Lütfen istediğiniz vade sayisini giriniz: ")) 
print(type(vade))
vade = (vade + 12)

# string interpolation
# Seçtiğiniz vade sonucu ortaya çıkan vade
print("Seçtiğiniz vade sonucu ortaya çikan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çikan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çikan vade: {vade}")

isim = "ozlem" #input("İsminizi giriniz")
metin = "Merhaba {name}".format(name=123)
print(metin)

# f-string
metin=f"Hoşgeldiniz {1+1}"
print(metin)

# listeler
# döngüler
# fonksiyonlar

dizi = ["İhtiyaç Kredisi",10,5.2,True]
print(dizi)

krediler = ["İhtiyaç Kredisi","Taşit Kredisi","Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #length
# print(krediler[3])=>hata verir

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşit Kredisi") 
print(krediler)


krediler.remove("Taşit Kredisi") #ilk gördüğü elemanı siler
print(krediler)

krediler.extend(["Y Kredisi","Z Kredisi"])
print(krediler)

# for 
# i=0 i<10

for i in range(10):
    print("xx")
    print(i)
print("***********")

for i in range(5,10):
    print(i)

print("*************")
for i in range(0,51,10):
    print(i)
print("*************")

# for i in range(0.1,1,0.5):
    # print(i)
krediler = ["İhtiyaç Kredisi","Taşit Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("***********")
for i in range(len(krediler)):
    print(krediler[i])
print("************")


# sonsuz döngü
i=0
while i<10:
    print("x")
    i+=1
print("************")

while True:
    print("X")
    break

print("******* Son Döngü******")

i=0
kredilerr = ["İhtiyaç Kredisi","Taşit Kredisi","Konut Kredisi"]
while i < len(krediler): 
     i+=1
     print(i)
     print(krediler[i])
     if krediler[i]=="Konut Kredisi":
        break
    
# fonksiyonlar

fiyat = 100
indirim = 20

# definition
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)


def sayHello(name):
    print(f"Merhaba {name}")


calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")


def calculateAndReturn(price,discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)

# void
def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price-discount

print("***************")
fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(f"159. satir: {fonk1}")
print(f"160. satir: {fonk2+100}")
print("***********")


# sınıflar=>classlar
# modules
# paket yönetimi
# self =>this tanımlanmış yapıyor gibi


#  instance => örnek
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)

