"""
Write a program to calculate electricity bill:

Units ≤ 100 → ₹1/unit

Units ≤ 200 → ₹2/unit

Units > 200 → ₹5/unit
"""
unit=float(input("Enter a electricity unit:-"))
if unit<=100:
    bill=unit*1
elif unit<=200:
    bill=unit*2
else:
    bill=unit*5
print("Electricity Bill is:-",round(bill,2))