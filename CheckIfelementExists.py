list = [ 1, 6, 3, 5, 3, 4 ]
print(f"The given list is: {list}")
key = int(input("Enter an element to be searched: "))
if(key in list):
    print(f"Key element {key} is present")
else:
    print(f"Key element {key} is not present")