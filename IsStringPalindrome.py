str = input("Enter string to check whether its palindrome or not: ")
temp = str[::-1]
if(str==temp):
  print(f"The given string '{str}' is a palindrome")
else:
  print(f"the given string '{str}' is not a palindrome")