def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
num=int(input("enter the number to chect factorial : "))
if num<0:
    print("Enter positive number")
elif num ==0:
    print( "Factorial  of 0 is 1 ")
else:
    print( f"factorial of {num} is {fact(num)}")