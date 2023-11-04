n=int(input("enter number for length of range of pattern:"))
for i in range(1,n):
    for j in range(n-i):
        print(i,end='')
    print()