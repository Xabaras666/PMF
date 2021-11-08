n = int(input())

#red po red... 
for i in range(n):
    #ispisujemo svaki red...
    for j in range(n):

        #gledamo udaljenost polja od "zidova"
        x = min(i, j, n-1-i, n-1-j)

        #tu udaljenost pretvorimo u slova
        znak = chr(ord('A') + x)
        
        print(znak, end='')
        
    #preci u novi red
    print ()