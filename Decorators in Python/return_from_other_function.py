def add1(x):
    def add2(y):
        return x + y
    return add2
s =add1(45)
print(s(5))