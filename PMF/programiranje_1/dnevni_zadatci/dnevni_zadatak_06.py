#Kreirati digitron. Od korisnika se traži da unese dva cijela broja. 
# Nakon unosa, program ispisuje sumu, razliku, proizvod i kolicnik unesenih brojeva.

a = int(input("Unesite jedan cijeli broj: "))
b = int(input("Unesite drugi cijeli broj: "))

print (f"Zbir: {a + b}")                #zapis pomocu f stringa
print (f"Razlika: {a - b}")
print ("Proizvod: ", a * b)             
print ("Kolicnik: ", float(a / b))      #float smo stavili iz razloga jer rezultat moze biti decimalan broj