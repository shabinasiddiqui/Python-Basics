def Sum(n):
    sum=0
    if n>=1:
        for i in range(1,n+1):
            sum=sum+(i*i)
        return sum
    else:
        print(f"Given number {n} is not a natural number: ")
        
        
n = int(input("Enter a number: "))
print(f"Sum of square of first {n} natural numbers: {Sum(n)}")
