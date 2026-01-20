# string
name="omkar"
print("Hello",name)

# print-he said ,"I want to eat an Apple"
print("he said,\"I want to eat an Apple\".")

# multiple line of string("""_ _ _ _""" or '''_ _ _ _''')
string="""hi.
how are you?
I am Fine.you?
I am good"""
print(string)

# Indexing
print("\t****Indexing****")
print("character at index 2 is",name[2])
# print("Character at index 7 is:-",name[7])  this shows error (index error)

# print all character from string one by one
for char in name:
    print(char)
length=len(string)
print("length of string variable is:-",length)
for i in range(length):
    print("character at index",i,"is-",string[i])

# Day12
# slicing of string
print("\t****Slicing****")
# frist two letter from name="omkar"
print("Frist two letter from word is:-",name[0:2])
# negative index   o m k a r
#                 -5-4-3-2-1
nm="omkar"
print("negative indexing:-",nm[-4:-2])# negative indexing 

# Day 13
# String method
