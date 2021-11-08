bodovi_vjezbe = float(input("Unesite bodove sa vjezbi: "))
bodovi_parcijale = float(input("Unesite bodove sa parcijale: "))
bodovi_zavrsni = float(input("Unesite bodove sa zavrsni: "))

ukupno = bodovi_vjezbe + bodovi_parcijale + bodovi_zavrsni

if ukupno >= 95:
    print("Ocjena 10")
elif ukupno >= 85:
    print("Ocjena 9")
elif ukupno >= 75:
    print("Ocjena 8")
elif ukupno >= 65:
    print("Ocjena 7")
elif ukupno >= 55:
    print("Ocjena 6")
else:
    print("Ocjena 5")


