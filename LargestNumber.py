n = int(input("Enter length of an array: "))
arr=[]
for i in range(0,n):
    arr.append(int(input(f"Enter {i+1}th element of array: ")))
    max = arr[0]
for i in range(0,n):
    if max<arr[i]:
        max=arr[i]
    
print(f"Largest number in a given thearray: {max}")