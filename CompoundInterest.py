#total amount Amount - Principal
R = float(input("Enter rate of interest: "))
T = int(input("Enter time period: "))
P = int(input("Enter Principal amount: "))
A = float(P*(1+R/100)**T)
ci = print(f"Compound Interest : {A-P}")