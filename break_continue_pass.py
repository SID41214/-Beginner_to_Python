available =10
x=int(input("enter number of sweet needed ?  :  "))
i=1
while i<=x:
    if i >available:
        print("limit reached")
        break
    print( f"{i} sweet")
    i+=1
print(" #########  bye  #########")