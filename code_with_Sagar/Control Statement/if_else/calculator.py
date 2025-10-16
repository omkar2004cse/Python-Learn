num_1=float(input("Enter a 1 Number:-"))
num_2=float(input("Enter a 2 Number:-"))

choice=input("Input Which operation to perfrom on data is(eg- +,-,*,/,%,**,//):-")

if(choice=="+"):
    print(num_1,"+",num_2,"is:-",num_1+num_2)
elif(choice=="-"):
    print(num_1,"-",num_2,"is:-",num_1-num_2)
elif(choice=="*"):
    print(num_1,"*",num_2,"is:-",num_1*num_2)
elif(choice=="/"):
    print(num_1,"/",num_2,"is:-",num_1/num_2)
elif(choice=="%"):
    print(num_1,"%",num_2,"is:-",num_1%num_2)
elif(choice=="**"):
    print(num_1,"**",num_2,"is:-",num_1**num_2)
elif(choice=="//"):
    print(num_1,"//",num_2,"is:-",num_1//num_2)
else:
    print("Enter a vaild input")