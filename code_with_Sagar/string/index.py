# W.A.P to accept some string from the keyboard and display its character by index wise(both positive and negative index)
s=input("Enter a String:-")
for i in range(len(s)):
    print(f"Character at positive index{i} and negative index {i-len(s)} is:-{s[i]}")