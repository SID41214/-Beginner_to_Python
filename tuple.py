tup = (21,26,36,25,1,3,3,3,5)
#print( tup[3] )
a=tup.count(3)
print(a)
#it is ordered immutable collection of elemts
print(id(a))
b=a
print(id(b))
print(id(3))
