#Program racuna sumu niza od 5
#brojeve koje unosi korisnik

maks = 5
suma = 0.0

print ('Program racuna sumu.')
print (maks, 'brojeva koje cete unijeti.')

for brojac in range(maks):
    broj = int(input("unesite broj: "))
    suma = suma + broj

print ("Suma unesenih brojeva je: ", suma)