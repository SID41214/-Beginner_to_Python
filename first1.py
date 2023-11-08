# n=10
# i=0
# while 0<n:
#     i+=n
#     n-=1
# print(f"sum of first natural number is {i}")

# n=10
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum of first natural numbers is",sum)
# def check(n):
#     if n & 1==0:
#         return "even"
#     else:
#         return "odd"
# n=11656481
# print(check(n))
# def fib(n):
#     fs=[]
#     a,b=0,1
#     count=0
#     while count<n:
#         fs.append(a)
#         a,b=b,a+b
#         count+=1
#     return fs
# print(fib(9))
# b="11001"
# a=int(b,2)
# print(a)
# c=bin(25)
# print(c)
# a=1
# b=2
# a,b=b,a
# print(a)
# print(b)
# h=10
# for i in range(h):
#     print(" "*(h-i),"*"*(2*i-1))
# for i in range(h-2,-1,-1):
#     print(" "*(h-i),"*"*(2*i-1))
# n=7
# for i in range(2,n):
#     if n%i==0:
#         print("not")
#         break
# else:
#     print("yes")

# def main(fun):
#     def wrap():
#         res=fun()
#         return res.lower()
#     return wrap
# @main
# def name():
#     return "HELLOOOOOOOOOOOOOOOOOOOP"

# print(name())
# class car:
#     wheels = 4
#     def __init__(self):
#         self.milage=15
#         self.color='red'
# c1=car()
# c2=car()
# c2.color='blue'
# print(c1.color)
# print(c2.color)
# print(c2.wheels)
# class dog:
#     def speak(self):
#         print("wolf")
# class cat:
#     def speak(self):
#         print("meow")
class A:
    _a=10
    __b=11
    def show(self):
        print(self._a)
        print(self.__b)
obj=A()
obj.show()
print(obj._a)
print(obj.__b)