def interchange(list):
    n = len(list)
    temp = list[0]
    list[0]=list[n-1]
    list[n-1]=temp

list = []
n = int(input("Enter length of the list: "))
for i in range(0,n):
    list.append(int(input()))
interchange(list)
print(list)