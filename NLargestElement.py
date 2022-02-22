list = [81, 52, 45, 10, 3, 2, 96] 
k = int(input("Enter a number: "))
new_list =[]

for i in range(0,k):
    max = 0
    for j in range(len(list)):
        if list[j] > max:
            max = list[j]
    list.remove(max)
    new_list.append(max)


#finding K largest element
print(f"Largest {k} elements in the given list are: {new_list}")