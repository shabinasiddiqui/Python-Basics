def interchange(list,index1,index2):
    list[index1],list[index2]=list[index2],list[index1]

list = []
n = int(input("Enter length of the list: "))
index1= int(input("Enter index 1 of values to be swapped: "))
index2 = int(input("Enter index 2 of values to be swapped: "))
print("Enter Elements of in an array: ")
for i in range(0,n):
    list.append(int(input()))
interchange(list,index1,index2)
print(list)