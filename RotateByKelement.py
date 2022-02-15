def Rotate(arr,n,k):
    temp=[]
    i=0
    while i<k:
        temp.append(i)
        i+=1
    i=0
    while k<n:
        arr[i]=arr[k]
        i=i+1
        k=k+1
    arr[:] = arr[: i] + temp
    return arr
  


k = int(input("Enter k: "))
n =int(input("Enter Length of an array: "))
arr = []
for i in range(0,n):
    arr.append(int(input(f"Enter {i+1}th element of an array: ")))

print(Rotate(arr,n,k))
