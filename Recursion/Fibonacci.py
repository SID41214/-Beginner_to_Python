def fun(n):
    if n<=1:
        return 1
    else:
        return(fun(n-1)+fun(n-2))
terms =10
if terms<=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Series :")
for i in range(terms):
    print(fun(i))