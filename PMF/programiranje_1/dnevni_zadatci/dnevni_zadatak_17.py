#Za broj 1 kažemo da je super broj. Ukoliko je neki broj x super, 
# tada su i brojevi 2x i 3x super. Na primjer, kako je broj 1 super, 
# tada su super brojevi 2 i 3. Kako su 2 i 3 super, tada su superi 
# brojevi 4, 6 i 9 itd. Istovremeno,brojevi 10 i 7 nisu super. 
# Napisati program koji od korisnika traži unos prirodnog broja n. 
# Program ispisuje da li je uneseni broj super.
import math
x = int (input('Unesite jedan prirodan broj x: '))

y = 1
pascal = [1]

while y <= x:
    z = y
    while z <= x:
        z *= 3
        pascal.append(z)
    y *= 2
    pascal.append(y)

if x in pascal:
    print('Uneseni broj je super broj.')
else:
    print('Uneseni broj nije super broj.')