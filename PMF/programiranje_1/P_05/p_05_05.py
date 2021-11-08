#!/bin/python3

import random

# int 0 <= x < 10
print('random.randrange(10):', 
       random.randrange(10))
       
# int 0 <= x <= 4
print('random.randint(0, 4):', 
       random.randint(0, 4))
       
# nasumicni [1, 3, 5, 7, 9]
print('random.randrange(1, 10, 2):', 
       random.randrange(1, 10, 2))

# float 0.0 <= x < 1.0
print('random.random():', 
       random.random())

# float 1.2 <= x < 18.0
print('random.uniform(1.2, 18.0):', 
       random.uniform(1.2, 18.0)) 