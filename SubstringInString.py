from operator import is_

str = input("Enter a string: ")
sub_str =input("Enter a substring to check whether its present in the string or not: ")

if str.count(sub_str)>0:
  print(f"{sub_str} is present")
else:
  print (f"{sub_str} is not present")
