import math
def f():
    n = int(input("enter number to be checked:"))
    c = 1
    for i in range (2,math.floor(math.sqrt(n))):
        if n % i == 0:
            c = 0
            break
    if c == 0 :
        print(n," is not prime")
    else:
        print (n," is prime")
