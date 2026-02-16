try:
    n1=int(input("enter a 1 number:-"))
    n2=int(input("enter a 2 number:-"))
    try:
        n=n1/n2
        print(f'result is:- {n}')
    except ZeroDivisionError:
        print("Check the number 2 is zero")
except ValueError:
    print("Gives the input as Integer")