#Napisati program koji za uneseni brojn ispisuje matricu 
# dimenzija n×n. Matrica sadrži brojeve od 1 do n**2 kao 
# u primjeru ispod za n=6.Svaki broj u matrici zauzima jednak 
# broj mjesta. Koristi se jedan znak više od broja znakova 
# koje zauzima najveci broj u matrici. U primjeru ispod,
# svaki znak zauzima tacno tri mjesta.

#  1  2  3  4  5  6
# 12 11 10  9  8  7
# 13 14 15 16 17 18
# 24 23 22 21 20 19
# 25 26 27 28 29 30
# 36 35 34 33 32 31

n = int(input("Unesite broj n: "))
l = []
x = 1
y = 10
for i in range(1, n ** 2 + 1):
    l.append(i)

for i in range(0, n,):
    for j in range(0, n):
        print(min(l), end=' ')
        while max(l) > y and min(l) :
            print(end=' ')
            y *= 10
        l.remove(min(l))
    print()




y = 10
for i in range(n):
    for j in range(n):
        print(x, end=' ')
        if x < y:
            print(end=' ')
        x+= 1
        y *= 10

    print()

        