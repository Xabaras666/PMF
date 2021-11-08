#Napisati program koji od korisnika traži unos prirodnog broja n.  
# Zatim,program od korisnika traži unos dva cijela broja a i b, 
# te generiše n slucajnih cijelih brojeva vecih od min(a,b)
# i manjih od mix (a,b),te ispisuje zbir pretposljednjih cifara svih generisanih brojeva. 
# Ukoliko korisnik unese broj 5, te racunar generiše brojeve: 9310, 341212, 32, 2920 i 238, 
# program ispisuje 10 (jer je 1+1+3+2+3 = 10).

import random

n = int(input("Unesite prirodan n: "))
a = int(input("Unesite cijeli broj a: "))
b = int(input("Unesite cijeli broj b: "))

l  = []
for i in range (n):
    i = random.randrange(a, b)
    l.append(i)

#print (l)

l1 = []
for i in l:
    i1 = (i %100) //10
    l1.append(i1)

#print(l1)
print ("Broj je:", sum(l1))