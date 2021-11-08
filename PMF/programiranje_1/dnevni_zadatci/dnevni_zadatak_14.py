#Program od korisnika traži da unese šest cijelih brojeva koji predstavljaju koordinate vrhova trougla u ravni.  
#Prva dva broja su koordinate x i y za prvu, iduca dva za drugu i posljednja dva za trecu tacku.  
#Program provjerava da li su unesene tacke kolinearne. Ukoliko jesu, program ispisuje #odgovarajucu poruku i ne radi više ništa. 
#Ukoliko tacke nisu kolinearne,one cine trougao. Nakon toga, od korisnika se ocekuje da unese koordinate još jedne tacke u ravni,te provjerava da li se unesena tacka nalazi u trouglu.

#Nekoliko napomena
# Za tri tacke kažemo da su kolinearne ukoliko leže na istoj pravoj.•
# Važno!Racunari realne brojeve ne cuvaju precizno kao što mi mislimo.Cesto se desi da se dva #nama jednaka broja, za racunar razlikuju u nekoj 20.  decimali. Stoga, ti brojevi racunaru #nisu jednaki. Kada želite porediti realne brojeve, nije mudro koristiti operator "= =".Mnogo #je bolje provjeriti da li je razlika ta dva broja manja od npr.0.00000001 i veca od #-0.0000001. Kao što je receno, za rješenje zadatka bi trebalo da koristite površine trouglova. 
# Za racunanje površina koristite formulu:P=1/2·|x1·(y2−y3) +x2·(y3−y1) +x3·(y1−y2)| Za #racunanje apsolutne vrijednosti 
# možete koristiti funkciju iz modula math. Drugi nacin je da sami isprogramirate simulaciju #ove funkcije (ako je broj 
# manji od nula, apsolutna vrijednost je minus taj broj).•  Nacrtajte slike i vidite šta u #kojem slucaju mora da vrijedi!

import math

x1 = int(input("Unesite broj x1: "))
y1 = int(input("Unesite broj y1: "))
x2 = int(input("Unesite broj x2: "))
y2 = int(input("Unesite broj y2: "))
x3 = int(input("Unesite broj x3: "))
y3 = int(input("Unesite broj y3: "))

e = 2.220446049250313e-16
#e = 0.000000000000001
p = 1/2 * abs( x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


if p < e:
	print("Unesene tocke su kolinearne.")
else:
	x4 = int(input('Unesite broj x4: '))
	y4 = int(input('Unesite broj y4: '))

	p_2 = 1/2 * abs( x1 * (y2 - y4) + x2 * (y4 - y1) + x4 * (y1 - y2))
	p_3 = 1/2 * abs( x1 * (y4 - y3) + x4 * (y3 - y1) + x3 * (y1 - y4))
	p_4 = 1/2 * abs( x4 * (y2 - y3) + x2 * (y3 - y4) + x3 * (y4 - y2))
	p_x = p_2 + p_3 + p_4

	if p_x - p < e and p -p_x < e:
		print ("Tocka 4 se nalazi unutar trokuta.")
	else:
		print ("Tocka 4 se nalazi izvan trokuta.")
