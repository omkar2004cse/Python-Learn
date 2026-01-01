# Write a program to check whether a number is positive or negative.
n=int(input("Enter a Number:-"))
if(n==0):
    print("Number is Not Positive or Not Negative")
elif(n>0):
    print(n,"Number is Positive")
else:
    print(n,"Number is Negative")