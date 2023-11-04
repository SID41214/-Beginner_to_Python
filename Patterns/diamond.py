h=int(input("enter height of diamond"))
for i in range(h):
    print(" "* (h-i), "*" *(2*i +1 ))
for i in range(h-2,-1,-1):
    print(" "*(h-i),"*" * (2*i+1))
    
    