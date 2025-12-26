# Write a program to find the smallest of three numbers.
num1=int(input("Enter a Frist Number:-"))
num2=int(input("Enter a Second Number:-"))
num3=int(input("Enter a Third Number:-"))
if num1==num2==num3:
    print(num1,num2,num3,"are equal")
elif num1<num2:
    if(num1<num3):
        print(num1,"is Smallest than",num2,num3)
    else:
        print(num3,"is Smallest than",num1,num2)
else:
    if(num2<num3):
        print(num2,"is Smallest than",num1,num3)
    else:
        print(num3,"is Smallest than",num1,num2)