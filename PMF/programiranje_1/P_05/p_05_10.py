#!/bin/python3

import random
from math import sqrt

BROJ_SIM = 10000
unutar_kruga = 0

for _ in range(BROJ_SIM):
	x = random.random()
	y = random.random()
	if sqrt(x*x + y*y) <= 1:
		unutar_kruga += 1
pi = 4 * (unutar_kruga/BROJ_SIM)
print(pi)