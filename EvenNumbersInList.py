def IsEven(list, new_list): 
    for i in range(0,len(list)):
        if list[i]%2==0:  
            new_list.append(list[i])
    
new_list=[]
list = [ 4, 6, 3, 5, 2, 1, 2, 7, 5, 64, 14] 
IsEven(list, new_list)
print(f"Even numbers in the given string are: {new_list}") 
