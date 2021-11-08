# Program ispisuje porez na imovinu

KOEFICIJENT = 0.0065   # Represents the tax factor.

print('Unesite broj parcele')
print('ili  0 za kraj.')
parcela = int(input('Broj parcele: '))

while parcela != 0:
    
    vrijednost = float(input('Unesite vrijednost imovine: '))

    porez = vrijednost * KOEFICIJENT

    print('Porez na imovinu: €', porez, sep='')

    # Uzmi broj naredne parcele
    print('Unesite broj naredne parcele')
    print('ili 0 za kraj.')
    parcela = int(input('Broj parcele: '))
    
print('Kraj programa.')