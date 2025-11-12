# checking the email is valid or not
mail=input("Enter a Your Email:-")
if '@' in mail and '.com' in mail:
    print("it is valid email")
else:
    print("Please Re enter a Mail")