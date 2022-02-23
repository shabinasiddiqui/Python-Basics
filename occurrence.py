list1 = [ 4, 6, 3, 5, 1, 1, 1, 7, 5, 1, 14] 
key = int(input("Enter a number to find its occurrence: "))
count=0
for i in range(len(list1)):
    if key==list1[i]:
        count+=1
print(f"{key} occurs {count} times")