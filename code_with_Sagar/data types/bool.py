# numeric datatype:- int,float,complex
# Boolean Datatype: True,False,Logical operation

# sequenced datatype:- string,list,tuple
# unordered datatype:- set, dictionary

# none:-absence of value

# boolean gives false answer when the input is 0 otherwise is always true
a=-2
print(type(a))
a=bool(a)
print(type(a),a)


# complex datatype
c=complex(input())
print(c.real,c.imag)
 

a=12
b=43
if type(a)==type(b):
    print("Done")
else:
    print("Wrong")