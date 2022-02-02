def fact(n):
    if n==1:
        return n
    else:

        return n*fact(n-1)


num = int(input("Enter a number: "))
if num<0:
    print("Factorial doesn't exist for negative number: ")
elif num==0:
    print(f"Factorial of {num}: 1")
else:
    print(f"factorial of {num}: {fact(num)}")

