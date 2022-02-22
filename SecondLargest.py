list = [ 4, 6, 3, 5, 2, 1 ]
max = list[0] 
second_largest=list[0]

# First find largest element
for i in list[1:len(list)]:
    if i>max:
        max=i

#inorder to find second largest element exclude largest element from given list
for i in list[1:len(list)]:
    if i>second_largest and i!=max:
        second_largest=i
print(f"Second largest element: {second_largest}")      
