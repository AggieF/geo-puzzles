# https://www.geocaching.com/geocache/GC5CH5V_project-euler-4

def ispalindrome(m):
    "Determines if a number is a palindrome"
    if str(m) == str(m)[::-1] : # checks if reverse string equals the string
        return True
    else:
        return False

def f(i,n):
    "Finds the first i digits of the largest palindrome made from the product of two numbers from 100 to n"
    Plist = []
    for j in range(100,n+1,1):
        for k in range (100,n+1,1): # loops over all these numbers
            P = j*k # multiples the two numbers
            if ispalindrome(P) == True:
                Plist.append(P)
    ans = str(max(Plist)) # the largest palindrome
    return int(ans[:i]) # the first i digits of the largest palindrome


print(f(2,747)) #52
print(f(2,390)) #12
print(f(3,750)) #535
print(f(3,615) - f(3,564)) #0
print(f(1,273)) #7
print(f(3,911)) #819

#Coordinates: N 52° 12.535' E 000° 07.819'
