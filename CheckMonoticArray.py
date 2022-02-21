def monotonic(arr):
    return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or
            all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))
  
n = int(input("Enter length of an array: "))
print("Enter elements in an array:")
arr =[]
for i in range(0,n):
    arr.append(int(input()))
if monotonic(arr):
    print("Array is monotonic")
else:
    print("Array is not monotonic")
