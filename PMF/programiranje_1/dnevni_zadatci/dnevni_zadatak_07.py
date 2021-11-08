#Neka je a prvi uneseni broj, te neka je b drugi uneseni broj u prethodnom zadatku. Nakon ispisa kolicnika, izracunati i ispisati vrijednosti izraza:

a = int(input("Unesite broj a: "))
b = int(input("Unesite broj b: "))

print ("a : b: ", a / b)
print (f"1. {a ** 2}")
print (f"2. {a ** 10}")
print (f"3. {a ** 100}")
print ("4. ", a ** b)
print ("5. ", a ** (1/2))
print ("6. ", a ** (1/b))
print ("7. ", (a ** 11) ** (1/b))