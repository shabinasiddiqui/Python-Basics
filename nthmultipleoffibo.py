def findPosition(k, n):
    first = 0
    second = 1
    i =2
    while i!=0:
        fib = first + second
        first = second
        second = fib
 
        if second%k == 0:
            return n*i
 
        i+=1
         
    return
 
 
n = 5
k = 4
 
print("Position of n\'th multiple of k in"
                "Fibonacci Series is", findPosition(k,n))
