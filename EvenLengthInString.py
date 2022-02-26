str = input("Enter a string: ")
new_str = str.split(' ')
temp=""

for i in range(len(new_str)):
  if len(new_str[i])%2==0:
    print(new_str[i])
    
# print(new_str)
