def Symmetric(str):
  low=0
  flag=0
  n =len(str)
  if n%2:
    mid = n//2 +1
  else:
    mid = n//2
      
  while (low<mid and mid<n):
    if str[low]== str[mid]:
      low+=1
      mid+=1
    else:
      flag=1
      break
    
  if flag==0:
    print("Entered string is Symmetric")
  else:
    print("Entered string is not Symmetric")


#main function
str = input("Enter string to check whether its Symmetric or not: ")
Symmetric(str)
  

  
