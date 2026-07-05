
n=int(input("enter number of terms"))
a=0
b=1
print(f"{a}{b}",end=" ")
for i in range(n):
    sum=a+b
    a=b
    b=sum
    print(sum,end=" ")