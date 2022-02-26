str = input("Enter a string to print words in reverse: ") 
words = str.split(' ')

for i in words[::-1]:
  print(i,end=" ")
    

