vjezbe = int(input("Unesite bodove iz vjezbi: "))
parcijalni = int(input("Unesite bodove iz parcijalnih ispita: "))
zavrsni = int(input("Unesite bodove iz zavrsnog: "))

bodovi = vjezbe + parcijalni + zavrsni
if bodovi < 55:
    print ("druze pao si")
elif 55 <= bodovi < 65:
    print ("Ocjena je 6")
elif 65 <= bodovi < 75:
    print ("Ocjena je 7")
elif 75 <= bodovi < 85:
    print ("Ocjena je 8")
elif 85 <= bodovi < 95:
    print ("Ocjena je 9")
elif 95 <= bodovi <= 100:
    print ("Ocjena je 10")
else:
    print ("pogresan unos")

