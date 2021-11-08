#Danas cemo se upoznati sa složenijim matematickim izrazima i njihovim
#racunanjem i zapisivanjem. U Python programiranju ne postoji razlomacka crta,
#ne postoje stepeni, ne možemo izostaviti znak množenja u2·a... 
#Sve ovo treba drugacije zapisati,te cemo u nastavku vidjeti kako se to
#radi. Za sada ne cemo koristiti stepenovanje, sinuse, kosinuse (. . . ),
#nego cemo se zadržati na pravilnom rasporedu zagrada i pravilnoj upotrebi
#matematickih simbola. Navedimo nekapravila:
#•Znak za množenje pišemo kao "∗". Ostale osnovne operacije se pišu
#standardno:+,−, /.
#•Ne smijemo izostavljati znak za množenje!
#•Izraz a(kroz)b pišemo kao(a)/(b). Zagrade su stavljene iz razloga što a i bmogu biti složeniji matematicki 
#izrazi (npr.(3+4∗12)/(23∗3−9)).
#•Srednja i velika zagrada se ne koriste u ovim izrazima. Stoga te zagrade mijenjamo sa malim zagradama. 
#Da bi najjednostavnije znali koje se zagrade uparuju sa kojima, možemo uvesti pravilo:svaka otvorena 
#zagrada se uparuje sa najbližom zatvorenom zagradom, ali samo ukoliko izmedju njih ne postoji druga 
#otvorena zagrada. Kada izvršimo uparivanje, te zagrade možemo zanemariti i postupak nastavljamo.
#•Uvijek moramo imati isti broj zatvorenih i otvorenih zagrada.
#•Za stepenovanje možemo primijeniti pravilo: a(na)b=a·a·a·. . .·a︸︷︷︸b.Mana ovoga pravila leži u 
#tome da je nemoguce b puta pomnožiti a ukoliko prije pocetka programa ne znamo koliko je b
# (npr. pri kodiranju digitrona ne znamo koji ce broj korisnik unijeti). U tomslucaju, koristi se operator∗∗,
#gdje je a∗∗b Python zapis za a(na)b.

# Zadatak
# Kreirajte program koji racuna i ispisuje vrijednost izraza:A=1/2+3/4+5/6+7/8+9/2(10)
# U novom redu ispišite vrijednost izraza ukoliko je umjesto 2(10) vrijednost 1(10).
# Testiranje.
# Za orginalni izraz rezultat treba da bude 0.379564. Za drugi izraz A poprima vrijednost 0.38057.

a = (1/(2+(3/(4+(5/(6+(7/(8+(9/(2**10))))))))))
a2 = (1/(2+(3/(4+(5/(6+(7/(8+(9/(1**10))))))))))
print (a)
print (a2)