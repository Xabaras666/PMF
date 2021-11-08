#Napisati program koji od korisnika traži da unese prirodan broj od 1 do 4.
    #Ukoliko korisnik unese broj 1, program od njega traži unos jednog realnog broja.
# Program  zatim  ispisuje  površinu  i  obim  kruga  sa unesenim poluprecnikom.

    #Ukoliko korisnik unese broj 2, program od njega traži da unese dva prirodna broja a i b, te vraca vrijednost površine 
# i obima pravougaonika sa unesenim stranicama.

    #Ukoliko korisnik unese broj 3, program od njega traži da unese realan broj a.  
#Program zatim provjerava da li je uneseni broj pozitivan, te ukoliko nije ispisuje odgovaraju cu poruku. 
# Inace program ispisuje površinu kvadrata sa unesenom stranicom.

    #Ukoliko korisnik unese broj 4, program od njega traži da unese dva cijela broja, te nakon toga program ispisuje podatak 
# o tome koji je broj veci (ili odgovarajucu poruku ukoliko su jednaki).

    #Ukoliko korisnik ne unese nijedan od iznad navedenih brojeva, program ispisuje poruku: Slusas li ti mene?

import math

a = int(input("Unesite prirodan broj od 1 do 4: "))

if a == 1:
    r = float(input("Unesite jedan realan broj za poluprecnik kruga: "))
    O = 2 * r * math.pi
    P = (r ** 2) * math.pi
    print ("Obim kruga je: ", O)
    print ("Povrsina kruga je: ", P)
elif a == 2:
    a_1 = int(input("Unesite prirodan broj a: "))
    b_1 = int(input("Unesite prirodan broj b: "))
    O_2 = 2 *a_1 + 2 * b_1
    P_2 = a_1 * b_1
    print ("Obim pravougaonika je: ", O_2)
    print ("Povrsina pravougaonika je: ", P_2)
elif a == 3:
    a_2 = float(input("Unesite realan broj a: "))
    if a_2 < 0:
        print("Uneseni broj je negativan.")
    else:
        print("Povrsina kvadrata je: ", a_2 * a_2)
elif a == 4:
    x = int(input("Unesite cijeli broj x: "))
    y = int(input("Unesite cijeli broj y: "))
    if x > y:
        print ("X je vece od Y.")
    elif y > x:
        print ("Y je vece od X.")
    else:
        print ("X i Y su jednaki.")
else:
    print("Slusas li ti mene?")
