# Calculator day7&8 
print("wel-come in calculator")
a=int(input("Enter a="))
b=int(input("Enter b="))
print("1)Addition\n2)Substraction\n3)Multiplication\n4)Division\n5)Reminder\n6)floor division\n7)Exponential")
print("enter a Your Choice:-")
c=int(input())
if c==1:
    print("Addition;-",a+b)
elif c==2:
    print("Substraction:-",a-b)
elif c==3:
    print("Multiplication:-",a*b)
elif c==4:
    print("Division:-",a/b)
elif c==5:
    print("Reminder:-",a%b)
elif c==6:
    print("Floor division:-",a//b)
elif c==7:
    print("Exponential:-",a**b)
else:
    print("Choose valid input")