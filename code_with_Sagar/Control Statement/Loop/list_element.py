# write a progrsm to tske input as the list and print each element of list by its index inmber
s=int(input("Enter a Size of List:-"))
l=[]
print("Enter a list element:-")
for i in range(s):
    l.append(int(input()))
for i in range(s):
    print("index",i,"element is:-",l[i])