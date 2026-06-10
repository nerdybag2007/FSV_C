import math 

n=int(input("enter anyvalid number till 10"))

for i in range(1,n+1):
    for j in range(1,n+1):
        if ((j==1)or (i==1 and j<n) or (i==n and j<n/2)  or (j==n and i>n/2) or (i==(n/2+1) and j>=n/2)):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    print()
