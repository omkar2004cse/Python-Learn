# if-else,elif,ifelse ladder
age=int(input("Enter a your age:-"))
if(age>18):
    print("You are eligible for vote")
elif(age==18):
    print("Wait for one Year to give vote")
else:
    print("You are not eligible for vote")
# conditional operator are :- >,<,==,>=,<=,!=
print("\t****Nested Ifelse****")
num1=int(input("Enter a 1st number:-"))
num2=int(input("Enter a 2nd number:-"))
num3=int(input("Enter a 3rd number:-"))
# if(num1>num2):
#     if num1>num3:
#         print("1st number is greater")
#     else:
#         print("3rd number is greater")
# else:
#     if num2>num3:
#         print("2nd number is greater")
#     else:
#         print("3rd number is greater")
if num1>num2 and num1>num3:
    print("1st Number is greater")
elif num2>num1 and num2>num3:
    print("2nd Number is greater")
else:
    print("3rd number is greater")



