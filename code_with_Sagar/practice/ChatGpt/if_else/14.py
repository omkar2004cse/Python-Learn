# Write a program to check whether a given number is divisible by both 3 and 7
num=int(input("Enter a Nummber:-"))
if num%3==0 and num%7==0:
    print(num,"is Divisible by both 3 and 7")
elif num%3==0:
    print(num,"is Divisible by 3 only")
elif num%7==0:
    print(num,"id Divisible by 7 only")
else:
    print(num,"is Not Divisible both 3 and 7")