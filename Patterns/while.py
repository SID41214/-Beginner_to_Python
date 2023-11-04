n=5
i,j=1,0
while (i<=n):
    while (j<=i-1):
        print("*",end='')
        j+=1
    print()
    j=0
    i+=1

print("============================================")
    
for i in range(6):
    for j in range(i):
        print("*",end='')
    print()

print("============================================")

 