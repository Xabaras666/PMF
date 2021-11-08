#f(x)= {-1  x<= -2
#      {1/3+(2/X)   0<x<=100
#      {200     x>=105
#      {0   inace

x = int(input("x: "))

r = 0

if x <= -2:
    r = -1
elif 0 < x <= 100:
    r = 1/(3+2/X)
elif x >= 105:
    r = 200
else:
    r = 0
print (r)