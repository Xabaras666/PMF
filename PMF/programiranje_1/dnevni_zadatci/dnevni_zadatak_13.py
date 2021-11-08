#Napišite program koji traži da se sa tastature unesu tri realna broja, a koji zatim ispisuje da li ta tri #broja mogu biti stranice pravouglog trougla. Pri unosu se ne zna koji je od tri unesena broja najveći 
#(koji je hipotenuza). Program treba da ponudi potvrdan odgovor za svaku od trojki (4,3,5), (3,4,5). . .1.
#Obavezno testirati program na ulaznim podacima 0.0003,0.0004 i 0.0005.Poredak unošenja nije važan. 
#Zašto se mogu javiti problemi u ovom slučaju? Ukoliko i dalje sve bude radilo OK, dodajte po jednu nulu. Pa opet...

a = float(input("Unesite realni broj a: "))
b = float(input("Unesite realni broj b: "))
c = float(input("Unesite realni broj c: "))

e = 0.0000000000000001
#print (type(e))

if (c ** 2) - (a ** 2 + b ** 2) < e and (a ** 2 + b ** 2) - (c ** 2) < e:
	print ("Uneseni brojevi MOGU biti stranice pravouglog trokuta.")
elif (a ** 2) - (b ** 2 + c ** 2) < e and (b ** 2 + c ** 2) - (a ** 2) < e:
	print ("Uneseni brojevi MOGU biti stranice pravouglog trokuta.")
elif (b ** 2) - (a ** 2 + c ** 2) < e and (a ** 2 + c ** 2) - (b ** 2) < e:
	print ("Uneseni brojevi MOGU biti stranice pravouglog trokuta.")
else:
	print ("Unesenu brojevi NE MOGU biti stranice pravouglog trokuta.")
	
	#nepravilan zadatak zbog 0.0000n
#if c ** 2 == a ** 2  + b ** 2 or a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2:
#	print ("Uneseni brojevi mogu biti stranice pravouglog trokuta.")
#else:
#	print ("Uneseni brojevi ne mogu biti stranice pravouglog trokuta.")

#5.6 - a < 0.0000000001 and a - 5.6 < 0.0000000001
