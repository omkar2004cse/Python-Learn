# break is stop the loop in some condition
print("Break:-") 
for i in range(1,11):
    if(i==7):
        break
    else:
        print(i,end=' ')


# continuse is skip these condition true and continue the iteration
print("\nContinue:-")
for i in range(1,11):
    if(i==6):
        continue
    else:
        print(i,end=" ")

# pass