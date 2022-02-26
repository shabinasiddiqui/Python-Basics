str = input("Enter a string: ")
k = int(input("Enter position of string to be removed: "))
new_str=""
for i in range(len(str)):
  if i!=k:
    new_str+=str[i]
print(new_str)
