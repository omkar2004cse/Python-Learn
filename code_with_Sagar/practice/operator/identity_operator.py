#  is and is not
a=12
b=12
print(id(a))
print(id(b))

print(a is b)

c=a
print(id(c))
print(c is a)

d=32
e=23
print(d is e)
print(d is not e)