# num=int(input("Enter a Number to Skip From sequence is:-"))
# for i in range(1,101):
#     if(num==i):
#         continue
#     else:
#         print(i,end="  ")

start=int(input("Enter a Start Number:-"))
end=int(input("Enter a End Number:-"))
skip=int(input("Enter a Number to Skip in sequence is:-"))
if(start<end):
    if(start<skip<end):
        for i in range(start,end):
            if(skip==i):
                continue
            else:
                print(i,end="  ")
    else:
        print("Skip number is not present in sequence")
else:
    print("Enter a Valid Inputs")