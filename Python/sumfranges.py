import math
n=int(input("enter your number"))
sum1=0
sum2=0
for i in range(n+1):
    if(i%2==0):
        sum1=sum1+i
    else:
        sum2=sum2+i
print("sum=",sum1)
print("sumofodd=",sum2)