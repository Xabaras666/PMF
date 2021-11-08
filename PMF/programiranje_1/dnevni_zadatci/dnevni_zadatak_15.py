#Kreirati program koji ce simulirati rad bankomata.  Program na pocetku ispisuje 
# pozdravnu poruku i od korisnika traži da unese šifru.  Šifra je cetverocifren prirodan broj. 
# Program samo provjerava da li je šifra cetverocifren broj, te ukoliko jeste, 
# korisniku je dozvoljen pristup (nema detaljnije provjere). 
# Nakon "ulaza u sistem", program korisniku nudi više opcija:
#1.  Pregled stanja
# 2.  Uplata
# 3.  Isplata
# 4.  Izlaz
#Opcije su oznacene brojevima (1-4), te unos broja opcije usmjerava korisnika.
# Unos koji nije u navedenom opsegu prekida program."Pregled stanja" ispisuje 
# trenutno stanje na racunu (pretpostavimo da korisnik u pocetku ima 8550 novcanih jedinica).
#   "Uplata" omogucava korisniku da uplati iznos do 2000 novcanih jedinica. Vece uplate i uplate 
# manje od 0 nisu dozvoljene. Program ispisuje prikladnu poruku u slucaju nepravilnog unosa. 
# Ukoliko je unos zadovoljavajuci, korisnik ima pravo da izabere dvije opcije ’D’ ili ’N’, kao odgovor
#na pitanje: Želite li prikaz konacnog stanja? Ukoliko korisnik izabere prvu opciju, 
# prikazano je stanje racuna nakon uplate.
#"Isplata" omogucava korisniku da podigne novac. Korisnik smije podici 500 novcanih 
# jedinica više od trenutnog stanja na racunu. Vrijednost morabiti djeljiva sa 100. 
# Program ispisuje stanje racuna nakon izvršene transakcije. U slucaju pogrešnog unosa, 
# program javlja grešku. "Izlaz" samo ispisuje pozdravnu poruku i zahvaljuje korisniku na korištenju usluga.

stanje_racuna = 8550

sifra = int(input('Pozdrav! Unesite vasu lozinku: '))
if 999 < sifra < 10000 or sifra == 0000:                #treba popraviti za 0001 itd
    ulaz_u_sistem = int(input("1. Pregled stanja \n2. Uplata \n3. Isplata \n4. Izlaz:   "))
    if ulaz_u_sistem == 1:
        print (stanje_racuna, "KM")
    elif ulaz_u_sistem == 2:
        uplata = int(input('Unesite kolicinu uplate: '))
        if 0 < uplata < 2000:
            stanje_racuna = stanje_racuna + uplata
            a = input("Zelite li prikaz konacnog stanja? \nOdgovorite sa D ili N: ")
            if a == "D": 
                print (stanje_racuna)
            else:
                print('Izlaz.')
        else:
            print ("Unos mora biti od 0 do 2000KM. ")
    elif ulaz_u_sistem == 3:
        isplata = int(input('Unesite kolicinu isplate: '))
        if isplata < stanje_racuna + 500:
            if isplata % 100 == 0:
                stanje_racuna = stanje_racuna - isplata
                print(stanje_racuna)
            else:
                print('Pogresan unos.')
        else:
            print('Pogresan unos.')
    else:
        print ('Pogresan unos.')
else:
    print("Pogresna lozinka")
