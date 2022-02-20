def remainder(res,k):
    print(f"Remainder is : {res%k}")

def result(arr,k):
    mul=1
    for i in arr:
        mul*=i
    remainder(mul,k)


n = int(input("Enter length of an array: "))
k = int(input("Enter a number: "))
arr = []
print("Enter the elements in an array: ")
for i in range(0,n):
    arr.append(int(input()))
result(arr,k)