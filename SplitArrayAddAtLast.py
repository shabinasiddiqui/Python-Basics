def reverse(arr,low,high):
    while low<=high:
        temp = arr[low]
        arr[low]=arr[high]
        arr[high]=temp
        low+=1
        high-=1
    return arr

def rotate(arr,k):
    n = len(arr)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)



n = int(input("Enter length of an array: "))
k = int(input("Enter an index to split the array: "))
print("Enter elements in an array:")
arr =[]
for i in range(0,n):
    arr.append(int(input()))
rotate(arr,k)
for i in range(0,n):
    print(arr[i], end=" ")

    

