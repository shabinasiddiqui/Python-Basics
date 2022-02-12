import math

def IsPerfectSqr(num):
    z= int(math.sqrt(num))
    return z*z==num

def IsFibonacci(n):
   return IsPerfectSqr(5*n*n + 4) or IsPerfectSqr(5*n*n - 4)
    

n = int(input("Enter a number: "))
if (IsFibonacci(n) == True):
    print (n,"is a Fibonacci Number")
else:
    print (n,"is a not Fibonacci Number ")
