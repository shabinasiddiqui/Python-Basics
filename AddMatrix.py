row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
matrix1=[]
matrix2 = []
print("Enter values in first matrix row wise: ")
for i in range(row):                               
    a=[]     
    for j in range(col):                             
        a.append(int(input()))
        print(end="")
    matrix1.append(a)
    print()

print("Enter values in second matrix row wise: ")
for i in range(row):                               
    a=[]     
    for j in range(col):                             
        a.append(int(input()))
        print(end="")
    matrix2.append(a)
    print()


#print matrix1
print("first matrix: ")
for i in matrix1:
    print(i)
#print matrix2
print("second matrix: ")
for i in matrix2:
    print(i)
   

#addition of two matrices
res =[]
for i in range(row):
    b=[]
    for j in range(col):
        b.append(matrix1[i][j]+matrix2[i][j])
    res.append(b)
    print()

    #print result

print("Addition of two matrix: ")
for i in res:
    print(i)
    
