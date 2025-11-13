# create the calculator
print("This is calculator program:-")
a=float(input("Enter a Frist Number:-"))
b=float(input("Enter a Second Number:-"))
select=input("Please Select the symbol for performing the operation on data(+,-,*,/,**,//,%):-")
if select == "+":
    print(a+b)
elif select =='-':
    print(a-b)
elif select =='*':
    print(a*b)
elif select =="/":
    print(a/b)
elif select == "//":
    print(a//b)
elif select == "**":
    print(a**b)
elif select == "%":
    print(a%b)
else:
    print("Please the the symbol to perform operation on data")