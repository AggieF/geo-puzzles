# https://www.geocaching.com/geocache/GC5C5T2_project-euler-2

# IMPORTANT puzzle starts from 1&2 instead of 0&1
"""
def fib(m):
    "TOO SLOW - Recursively generates the m th Fibonacci number"
    if m == 0:
        return 1
    elif m == 1:
        return 2
    else:
        return Fib(m-1)+Fib(m-2)
"""

def Fib(M):
    "FASTER - Generates the M th Fibonacci number using a loop"
    a,b = 1,2
    for k in range(M):
        a,b = b, a+b
    return a

# print(Fib(0))

def euler_two(n):
    "when given number n, returns the sum of the first n numbers of the Fibonacci sequence even terms"
    S = 0
    i = 0
    j = 0 #counts only even terms of the Fibonacci sequence
    while (j <= n):
        if Fib(i)%2 == 0:
            S += Fib(i)
            i += 1
            j += 1
        else:
            i += 1
    return S

# IMPORTANT puzzle uses one indexing but python in zero indexing
a = 150
b = 516
c = 6506
d = 14
e = 24
f = 3232

print (euler_two(a-1))
print (euler_two(b-1))
print (euler_two(c-1))
print (euler_two(d-1))
print (euler_two(e-1))
print (euler_two(f-1))
