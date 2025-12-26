# Write a program to find the largest of two numbers.
n1=int(input("Enter a Frist Number:-"))
n2=int(input("Enter a Second Number:-"))
if n1==n2:
    print(n1,"and",n2,"is Equal")
elif n1>n2:
    print(n1,"is Greater than",n2)
else:
    print(n2,"is Greater than",n1)