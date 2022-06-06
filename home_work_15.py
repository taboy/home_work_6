#15.	Написать программу, получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[1, 2, 6, 24]

# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
import os
from itertools import accumulate
import operator
import random


n = int(input("write a number"))

print( *list(accumulate([x for x in range(1, n + 1)], operator.mul)), '\n')