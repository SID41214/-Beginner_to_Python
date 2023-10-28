def upper(fun):
    def wrap():
        r=fun()
        return r.upper()
    return wrap
def out():
    return "hello"

print(upper(out)())
print("\n****************\n other way \n**************")
#same in other way:

def upper1(fun):
    def wrap():
        r=fun()
        return r.upper()
    return wrap
def out1():
    return "hello"
f=upper1(out1)
print(f())
print("\n****************\n by decorators \n**************")
#same in other way:( By decorators)



def upper2(fun):
    def wrap():
        r=fun()
        return r.upper()
    return wrap

@upper2 # decorator and it will be in the following
def out2():
    return "hello"

print(out2())
