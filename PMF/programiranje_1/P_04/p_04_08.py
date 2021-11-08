# Program koji vrsi konverziju brzina
# od 60 kns u mns
#(inkrementi su 10 kns)

pocetna_brzina = 60
krajnja_brzina = 131
inkrement = 10
koeficijent = 0.6214

print ('KNS\tMNS')
print ('----------')

for kns in range (pocetna_brzina, krajnja_brzina, inkrement):
    mns = kns * koeficijent
    print(kns, '\t', mns)