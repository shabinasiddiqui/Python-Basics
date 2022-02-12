n = int(input("Enter Length Of An Array: "))
arr =[]
for i in range(0,n):
    x = int(input(f"Enter {i+1}th element of an array: "))
    arr.append(x)
print(f"Sum of Array: {sum(arr)}")