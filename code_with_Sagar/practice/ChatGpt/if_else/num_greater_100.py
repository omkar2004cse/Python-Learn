# Write a program to check whether a number is greater than 100 or not
n=int(input("Enter a Number:-"))
if(n==0):
    print("Number is Zero")
elif(n<0):
    print("Number is Negative")
else:
    if(n>100):
        print(n,"is Greater than 100")
    else:
        print(n,"is smaller than 100")
        