"""Write a program to calculate salary bonus:

Salary ≥ 50,000 → 10% bonus

Salary < 50,000 → 5% bonus"""

sal=int(input("Enter a Your Salary:-"))
if sal<50000:
    bonus=(50000*5)/100
else:
    bonus=(50000*10)/100

print("Your Bonus is:-",bonus)
print("Total Salary is:-",(sal+bonus))