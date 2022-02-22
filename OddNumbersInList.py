def IsOdd(list, new_list): 
    for i in range(0,len(list)):
        if list[i]%2==1:  
            new_list.append(list[i])
    
new_list=[]
list = [ 4, 6, 3, 5, 2, 1, 2, 7, 5, 64, 14] 
IsOdd(list, new_list)
print(f"Odd numbers in the fiven string are: {new_list}") 
