a = input()
#print (type(a))
#print (a == "")
#print (a == " ")
sum = 0

while a != '':
    a = int(a)
    sum += a
    a = input()
    print (sum)