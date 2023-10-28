def upper_decor(fun):
    def wrapper(n):
        result=fun(n)
        return result.upper()
    return wrapper

def attach_decor(fun):
    def wrapper(sent):
        result = fun(sent)
        length =len(result)
        result+= ' '+ str(length)
        return result
    return wrapper

@upper_decor
@attach_decor
def test(n):
    return 'hello '+n

print(test('sid'))