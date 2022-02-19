def reverse(arr,low,high):
    while low<=high:
        temp = arr[low]
        arr[low]=arr[high]
        arr[high]=temp
        low+=1
        high-=1

def rotate(arr,k):
    n =int(len(arr))
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)

n = int(input("Enter length of an array: "))
k= int(input("Enter Value Of K: "))
arr = []
print("Enter the elements in an array: ")
for i in range(0,n):
    x = int(input())
    arr.append(x)
rotate(arr,k)
for i in range(0,n):
    print(arr[i],end=" ")









