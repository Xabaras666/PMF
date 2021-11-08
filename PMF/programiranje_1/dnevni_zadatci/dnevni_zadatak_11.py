#Napisati program koji od korisnika traži unos petocifrenog prirodnog broja n. 
# Program provjerava da li je uneseni broj palindrom. 
# Za broj kažemo daje palindrom, ukoliko se jednako cita sa obje strane. 
# Neki od petocifrenih palindroma su 12321, 15651, 92929. Brojevi 12345 ili 12334 nisu palindromi.

#n1 = int(input("Unesite petocifreni broj1: "))
#n2 = int(input("Unesite petocifreni broj2: "))
#n3 = int(input("Unesite petocifreni broj3: "))
#n4 = int(input("Unesite petocifreni broj4: "))
#n5 = int(input("Unesite petocifreni broj5: "))

#if n1 == n5 and n2 == n4:
 #   print ("Broj je palindrom.")
#else:
  #  print ("Broj nije palindrom.")

n = int(input("Unesite petocifreni broj: "))

n1 = n // 10000
n2 = (n // 1000) % 10
n3 = (n // 100) % 10
n4 = (n // 10) %10
n5 = n % 10

if n1 == n5 and n2 == n4:
    print ("Uneseni broj je palindrom.")
else:
    print ("Uneseni broj nije palindrom.")