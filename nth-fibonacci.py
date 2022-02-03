n = int(input("Enter a number: "))
first,second=0,1
fibo_list=[0,1]
for i in range(2,n):
    fib = first+second
    fibo_list.append(fib)
    first=second
    second=fib
print(fibo_list[n-1])


    