# input function
name=input("Enter a your name:-")
print("Your name is:-",name)

print("\t****Frist way****")
a=input("input a frist number:-") # taking as input as string
b=input("input a second number")
# print("Substraction is:-",x-y) these shows error because they take input as string
print("Substraction is:-",int(a)-int(b)) # typecasting

x=int(input("input a frist number:-"))
y=int(input("input a second number:-"))
print("multiplication of",x,"*",y,":-",x*y)