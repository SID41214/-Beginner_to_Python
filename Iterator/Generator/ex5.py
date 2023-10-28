def fib(limit):
    a,b=0,1
    while a< limit:
        yield a
        a,b=b,a+b
x=fib(5)  # x is generator object 
print(next(x))
print(next(x))
print(next(x))

 # using for in loop
print("using for in loops")      
for i in fib(5):
    print(i)