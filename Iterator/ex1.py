list =[4,17,60,33]
my_iter=iter(list)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())