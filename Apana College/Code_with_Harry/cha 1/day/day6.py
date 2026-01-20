# variable and Data Type(int,string,float,none,boolean(bool),list,tuple,dictionary(dict))

a=1342
b="omkar"
c=True
d=None
e=complex(3,6)
print(a,type(a),sep="  ")
print(b,type(b),sep="  ")
print(c,type(c),sep="  ")
print(d,type(d),sep="  ")
print(e,type(e),sep="  ")
# type is inbuild function that is given type of variable data is stored

# List
li=[1,2.4,"omkar",["apple","mango","banana"],[1,11,34.56,"king"]] #list is collection of different data type and list contain another list
print(li,type(li),sep="  ")
# List are Mutable
li[2]="don"
print(li)

# Tuple
tup=(1,2.3,4.5,"omkar")
print(tup,type(tup))
tup1=1,2,3,4,6.88,4.54,"omkar"
print(tup1,type(tup1))
# Tuple is immutable (they shows error(tuple does not support item assignment))
# tup[3]=123
# print(tup)

# Mapped Data:- Dict(dictionary)
dic={"name":"Omkar","age:-":21,"Branch":"cse","CGPA:-":8.1}
print(dic,type(dic),sep="  ")
# dictionary Data type is Mutable
dic[2]={"Eligible for Vote":"Yes"}
print(dic)