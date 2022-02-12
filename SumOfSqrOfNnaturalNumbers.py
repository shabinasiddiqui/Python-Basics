def Sum(n):
    sum=0
    if n>=1:
        for i in range(1,n+1):
            sum=sum+(i*i)
        return sum
        
        
n = int(input("Enter a number: "))
print(f"Sum of first {n} natural numbers: {Sum(n)}")
