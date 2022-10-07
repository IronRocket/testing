import math
z = input("Find d, a1, n:")

if z == "d":
    a,n = input("Enter a of n(46,3):").split(",")
    a1 = input("Enter a of 1:")
    print("D:",(a-a1)/n-1)
elif z == "a1":
    a,n = input("Enter a of n(46,3):").split(",")
    d = input("Enter d:")
    print((a-(d*(n-1))))
else:
    a1 = input("Enter a of 1:")
    d = input("Enter d:")
    