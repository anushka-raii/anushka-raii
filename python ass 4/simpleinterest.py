#Simple Interest Calculator Take input for Principal (P), Rate of Interest (R), and Time in years (T). Write a program to calculate Simple Interest using the formula:SI = (P × R × T) / 100

P = float(input("Enter Principal: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time in years: "))

SI = (P * R * T) / 100
print("Simple Interest:", SI)
