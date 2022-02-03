def IsPrime(num):

    if num>1:
        for i in range(2,int(num/2)+1):
       
            if (num % i)==0:
                return False
        else:
            return True  
    else:
            return False


num = int(input("Enter a number: "))
if IsPrime(num)==True:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
