#!/bin/python3

import random

BROJ_SIM = 1000

r2, r3, r4, r5, r6, r7 = 0, 0, 0, 0, 0, 0
r8, r9, r10, r11, r12 = 0, 0, 0, 0, 0

for _ in range(BROJ_SIM):
  kockica1 = random.randrange(1, 7)
  kockica2 = random.randrange(1, 7)
  zbir = kockica1 + kockica2
  
  if   zbir == 2:  r2 += 1
  elif zbir == 3:  r3 += 1
  elif zbir == 4:  r4 += 1
  elif zbir == 5:  r5 += 1
  elif zbir == 6:  r6 += 1
  elif zbir == 7:  r7 += 1
  elif zbir == 8:  r8 += 1
  elif zbir == 9:  r9 += 1
  elif zbir == 10: r10 += 1
  elif zbir == 11: r11 += 1
  elif zbir == 12: r12 += 1
  else: print("Kako ovo?")


print(r2/BROJ_SIM*100, r3/BROJ_SIM*100, 
      r4/BROJ_SIM*100, r5/BROJ_SIM*100,
      r6/BROJ_SIM*100, r7/BROJ_SIM*100,
      r8/BROJ_SIM*100, r9/BROJ_SIM*100,
      r10/BROJ_SIM*100, r11/BROJ_SIM*100,
      r12/BROJ_SIM*100, sep='\n')
      
for _ in range(int(r2/BROJ_SIM*100)):
  print('*', end='')
print()
for _ in range(int(r3/BROJ_SIM*100)):
  print('*', end='')
print()
for _ in range(int(r4/BROJ_SIM*100)):
  print('*', end='')
print()
for _ in range(int(r5/BROJ_SIM*100)):
  print('*', end='')
print()
for _ in range(int(r6/BROJ_SIM*100)):
  print('*', end='')
print()
for _ in range(int(r7/BROJ_SIM*100)):
  print('*', end='')
print()
for _ in range(int(r8/BROJ_SIM*100)):
  print('*', end='')
print()
for _ in range(int(r9/BROJ_SIM*100)):
  print('*', end='')
print()
for _ in range(int(r10/BROJ_SIM*100)):
  print('*', end='')
print()
for _ in range(int(r11/BROJ_SIM*100)):
  print('*', end='')
print()
for _ in range(int(r12/BROJ_SIM*100)):
  print('*', end='')
print()
