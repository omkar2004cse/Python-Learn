# acess the each character of string in forward and backword direction  using while loop
s=input("Enter a String:-")
i=0
while i<len(s):
    print(i,s[i])
    i+=1
j=-len(s)
print("reverse String is:-")
while j<0:
    print(j,s[j])
    j+=1
