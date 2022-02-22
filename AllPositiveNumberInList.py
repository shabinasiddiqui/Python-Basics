def PositiveList(list):
    new_list=[]
    for i in range(len(list)):
        if list[i]>0:  
            new_list.append(list[i])
        
    print(f"Positive numbers in the given List are: {new_list}") 


list = [ 4, -6, 3, 5, -2, -1, 2, 7, 5, -64, 14] 
PositiveList(list)