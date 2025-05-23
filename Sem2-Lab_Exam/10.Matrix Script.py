#!/bin/python3
import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# code
transpose = ''.join([c for ls in zip(*matrix) for c in ls])
print(re.sub(r"(?<=\w)[!@#$%& ]+(?=\w)", " ", transpose))
