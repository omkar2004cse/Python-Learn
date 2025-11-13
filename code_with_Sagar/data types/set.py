# set is mutable but unordered
s=set([1,23,42,42,12,1,3,1,3,4,5,2])
print(s)
print(type(s))
s=s.add(54)
print(s)