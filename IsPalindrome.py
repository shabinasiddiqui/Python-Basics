num = int(input("Enter a number: "))
temp = num
rev=0
while(num>0):
    rev = rev*10 +(num%10)
    num=num//10
if rev==temp:
    print(f"{temp} is a palindrome number")
else:
    print(f"{temp} is not a palindrome number")
