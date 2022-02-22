def RemoveEle(list1,list2):
    list1= [i for i in list1 if i not in list2] 
    print(f"After deleting elements new list:{list1}")


list1 = [ 4, 6, 3, 5, 2, 1, 2, 7, 5, 64, 14] 
print(f"Before deleting elements new list:{list1}")
n = int(input("Enter length of an array: "))
print("Enter the Elements to be removed: ")
list2 =[]
for i in range(0,n):
    list2.append(int(input()))
RemoveEle(list1,list2)