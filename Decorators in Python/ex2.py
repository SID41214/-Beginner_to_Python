def triple_decor(fun):
    def wrapper(n):
        any_list=fun(n)
        return[i *3 for i in any_list]
    return wrapper




@triple_decor
def reverse_list(l):
    return l[::-1]

@triple_decor
def upper_list(l):
    return [i.upper() for i in l]

@triple_decor
def fibonacci(n):
    result =[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result
    
print(reverse_list([1,2,3]))
print(upper_list(['a','b']))
print(fibonacci(6))







