"""U trecem zadatku cemo kreirati "bezveze digitron". Ovaj digitron imaza cilj da simulira pravi,
 jednostavni digitron sa cetiri osnovne operacije,te da se studenti upoznaju sa idejom i potrebama 
 za unos podataka sa tastature. Za rješavanje ovoga zadatka je potrebno da studenti poznaju ispis teksta,
 osnovne operacije sa cijelim brojevima u Pythonu, te ispis brojnih izraza. Obratite pažnju i na ostale 
 matematicke operacije, poput ostatka ili cjelobrojnog djeljenja. """

# Zadatak 
# Kreirati digitron koji poznaje cetiri osnovne operacije. Program simulira jednostavne operacije 
# sa dva cijela broja. Nakon toga ispisuje sumu,razliku,proizvod i kolicnik neka dva broja.

a = int(input("Unesite cijeli broj a: " ))
b = int(input("Unesite cijeli broj b: "))

print ("a+b=", a + b)
print ("a-b=", a - b)
print ("a*b=", a * b)
print ("a/b=", float(a / b))