n=int(input("enter a number"))
sum=""
while n>0:
        r=n%10
        r=str(r)
        sum=sum + r
        n//=10
print(sum)    
