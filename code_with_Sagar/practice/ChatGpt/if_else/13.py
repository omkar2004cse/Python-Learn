# Write a program to check whether a student has passed or failed (Pass marks = 40).
mar=int(input("Enter a Marathi Mark:-"))
hin=int(input("Enter a Hindi Mark:-"))
eng=int(input("Enter a English Mark:-"))
math=int(input("Enter a Maths mark:-"))
sci=int(input("Enter a Science mark:-"))
total=mar+hin+eng+math+sci
print("Total Mark Obtained is:-",total)
avg=total/5
print("Percentage is Obtained is:-",avg)
if avg >=35:
    print("Student is Passed")
else:
    print("Student is Not Passed")