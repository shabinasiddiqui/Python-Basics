list = [ 6, 6, 3, 5, 2, 1 ]
min = list[0]
for i in list[1:len(list)]:
    if i < min:
        min =i
    else:
        i+=1
print(f"Smallest number in a given list: {min}")