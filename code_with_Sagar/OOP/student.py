class student():
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def s_detail(self):
        print(f'name is {self.name} and roll no is {self.roll_no} and its marks is {self.marks}')

s1=student("omkar",59,78.94)
s2=student("vivek",58,64)
s3=student("shailendra",25,67)
s4=student("shweta",13,65)

s1.s_detail()
s4.s_detail()

# marks is updated
s4.marks=98

s4.s_detail()
s3.s_detail()
s4.s_detail()