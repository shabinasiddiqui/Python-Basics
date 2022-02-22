def EvenList(start, end):
    new_list=[]
    for i in range(start,end+1):
        if start%2==0:  
            new_list.append(start)
        start+=1
    print(f"Even numbers in the given Range are: {new_list}") 
    
start = int (input("Enter the starting value of range: "))
end = int (input("Enter the ending value of range: "))

EvenList(start,end)