"""Write a program to calculate grade based on marks:

≥ 90 → A

≥ 75 → B

≥ 50 → C

< 50 → Fail"""

print("Wel-Come in Grade Calculator")
mar=int(input("Enter your Marathi mark:-"))
hi=int(input("Enter your Hindi mark:-"))
eng=int(input("Enter a your English mark:-"))
mat=int(input("Enter a your Maths mark:-"))
sci=int(input("Enter a your Science mark:-"))
t=mar+hi+eng+mat+sci
print("You get",t,"of 500")
avg=t/5
print("you get percentage is:-",avg)
if avg>=90:
    print("You get the \"A\" Grade")
elif 89>=avg>=75:
    print("You get the \"B\" Grade")
elif 74>=avg>=50:
    print("You get the \"C\" Grade")
else:
    print("You Fail in this Year")