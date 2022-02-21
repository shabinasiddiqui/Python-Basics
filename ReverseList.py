list = [ 10, 6, 3, 5, 2, 1 ]
print(f"List before reverse: {list}")
low,high = 0,len(list)-1
while low<=high:
    temp =list[low]
    list[low]=list[high]
    list[high]=temp
    low+=1
    high-=1

print(f"List after reverse: {list}")

