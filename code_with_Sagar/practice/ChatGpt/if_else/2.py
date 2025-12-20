# Write a program to check whether a number is even or odd.
num=int(input("Enter a Number:-"))
if(num==0):
    print("Number is Zero")
elif(num%2==0):
    print(num,"is Even")
else:
    print(num,"is Odd")