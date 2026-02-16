a=int(input("Enter a Number:-"))
try:
    num=int(input("Enter a n="))
    a=a/num
except ZeroDivisionError:
    print("a can not divide with the 0")

except ValueError:
    print("Please check the enter value")