# raise is used for the custom expection(manual Exception)

def pass_check(p):
    if (len(p)<8):
        raise Exception("Error is password is <8 character")
    print("Password is Strong")

try:
    pa=input("Enter a Password:-")
    pass_check(pa)

except Exception as e:
    print(e)