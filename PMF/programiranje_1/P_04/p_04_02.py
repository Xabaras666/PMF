#!/bin/python3
# Ovaj program računa proviziju prodavača

# Varijabla koja kontroliše ponavljanje.
nastavi = 'da'

# Računanje niza provizija.
while nastavi == 'da':

    prodaja = float(input('Unesite ukupan iznos prodaje: '))
    procenat = float(input('Unesite iznos vaše provizije: '))

    provizija = prodaja * procenat

    print('Vaša provizija je: €', provizija, sep='')

    nastavi = input('Da li zeliti izracunati jos jednu ' + \
                       'proviziju (unesite da ili ne): ')
                       
print('Kraj programa.')