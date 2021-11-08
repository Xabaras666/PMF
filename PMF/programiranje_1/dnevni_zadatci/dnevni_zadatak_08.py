#Napisati program koji narednim redoslijedom od korisnika uzima četiri realne 
# vrijednosti:α,n,k i h. Vrijednosti se unose jedna ispod druge. Program ispisuje 
# rezultat narednog izraza:
import math
alfa = float(input("Unesite vrijednost alfa: "))
n = float(input("Unesite vrijednost n: "))
k = float(input("Unesite vrijednost k: "))
h = float(input("Unesite vrijednost h: "))

alfa = alfa * (math.pi / 180 )

rjesenje = ((2 * k ** (2/3)) / (math.sin(alfa) * math.sqrt(h + n))) * math.cos(alfa)
print (rjesenje)