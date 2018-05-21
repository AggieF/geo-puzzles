# https://www.geocaching.com/geocache/GC57DV8_project-euler-1

def euler_one(n):
    "When given a natural number n, returns the sum of multiples of 3 or 5 which are less than n"
    S = 0
    for i in range(0,n):
        if i%3 == 0 or i%5 == 0:
            S += i
    return S


a = 4720
b = 240
c = 77
d = 175
e = 1000

N = euler_one(a) + euler_one(b) + euler_one(c)
E = euler_one(d) + euler_one(e)

print (euler_one(e))

#Coordinates: N 52°12.178' E 00°07.141'
