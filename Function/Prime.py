import math

def prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2 ==0:
        return False
    for i in range (3,int(math.sqrt(n))+1,2):
        if n %i  == 0:
            return False
    return True
print("BY normal funtion ::")
print(prime(6))
# BY LIST COMPREHENSION
def checkprime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    return all(n%i !=0 for i in range(2,int(math.sqrt(n))+1))
print("BY function with list comprehension ::")
print(checkprime(17))

