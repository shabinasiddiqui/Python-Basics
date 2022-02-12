def Sum(n):
    sum=0
    if n>=1:
        for i in range(1,n+1):
            sum+=(i**3)
        return sum
    else:
        print(f"Given number {n} is not a natural number: ")
        
        
n = int(input("Enter a number: "))
print(f"Sum of cube of first {n} natural numbers: {Sum(n)}")
