def sum(list,n):
    if n==0:
        return 0
    else:
        return list[n-1]+ sum(list,n-1)
    

list = [11, 5, 17, 18, 23]
total = sum(list,len(list))
print(f"Sum of the given list is : {total}")