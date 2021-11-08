#Programkoristi ponavljanje kako bi prikazalo tabelu brojeva od 1 do 10
#i njihove kvadrate

print ('Broj\Kvadrat')
print ("-------------")

for broj in range (1, 11):
    kvadrat = broj ** 2
    print (broj, "\t", kvadrat)