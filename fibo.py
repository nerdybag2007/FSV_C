n=int(input("enter te number "))
m=n
sum=0
for i in range (1,20):
    if n>0:
        r=n%10
        sum=sum + r**3
        n=n/10
        n=int (n)
if (sum==m):
    print("armstrong")
else:
    print("nice try")

