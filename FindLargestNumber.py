list = [ 6, 6, 3, 5, 2, 1 ]
large = list[0]
for i in list[1:len(list)]:
    if i > large:
        large =i
    else:
        i+=1
print(f"Largest number in a given list: {large}")