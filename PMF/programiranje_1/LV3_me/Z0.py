vjezbe = int(input("Unesite broj bodova sa vjezbi: "))
parcijalni = int(input("Unesite broj bodova sa parcijalnih: "))
zavrsni = int(input("Unesite broj bodova sa parcijalnih: "))

ukupni_broj_bodova = vjezbe + parcijalni + zavrsni

if ukupni_broj_bodova >=95 and ukupni_broj_bodova <= 100:
    print("Prosli ste sa 10.")
elif 85 <= ukupni_broj_bodova <= 94:
    print ("Prosli ste sa 9.")
elif 75 <= ukupni_broj_bodova <= 84:
    print ("Prosli ste sa 8.")
elif 65 <= ukupni_broj_bodova <= 74:
    print ("Prosli ste sa 7.")
elif 55<= ukupni_broj_bodova <= 64:
    print ("Prosli ste sa 6.")
elif ukupni_broj_bodova > 100 or ukupni_broj_bodova < 0:
    print ("Nisi ti to nesto")
else:
    print("Pali ste.")