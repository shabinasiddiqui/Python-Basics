num = int(input("Enter a number: "))
temp = num
a=0
while num>0:
    a =a + (num%10)**3
    num=num//10
if a==temp:
    print(f"{temp} is an Armstrong number")
else:
    print(f"{temp} is not an Armstrong number")

    

