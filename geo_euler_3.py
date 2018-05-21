# https://www.geocaching.com/geocache/GC5CH0M_project-euler-3

import numpy as np
from sympy.ntheory import factorint

"""
print(factorint(24)) #gives dict with exponents e.g. 24 = (2**3)*(3**1)
print(factorint(24, multiple=True)) #gives list with multiples e.g. 24 = 2*2*2*3
"""

def f(n):
    "finds the largest prime factor of n"
    list1 = np.array(factorint(n, multiple=True))
    L = np.max(list1)
    return L

def g(m):
    "finds the sum of all prime factors of m, including multiples"
    list2 = np.array(factorint(m, multiple=True))
    S = np.sum(list2)
    return S

A = 67108864
B = 36
C = 475262344414189
D = 0
E = 16
F = 17592567

print(g(A)) #52
print(g(B)) #10
print(f(C)) #877
print(D) #0
print(g(E)) #8
print(g(F)) #834

# Coordinates: N 52°10.877'  E 000°08.834'
