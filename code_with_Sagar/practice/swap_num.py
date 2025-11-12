# swap of two variable
v1=int(input("Enter frist Number:-"))
v2=int(input("Enter a Second Number:-"))
print("Before Swaping Number are",v1,v2)
print("After Swaping Number are:-")

# logic 1
# v1,v2=v2,v1
# print(v1,v2)


# using third variable
c=v1
v1=v2
v2=c
print(v1,v2)



# without third variable
# v1=v1+v2
# v2=v1-v2
# v1=v1-v2
# print(v1,v2)