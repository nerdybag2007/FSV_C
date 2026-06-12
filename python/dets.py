import math
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))

D=b**2-4*a*c

print(f"determinant= {D} ")

if D>0:
    print("two dist roots")
    choice=input("do you want to find roots(y/n)")
    if choice =="y":
        root1=(-b+math.sqrt(D))/(2*a)
        root2=(-b-math.sqrt(D))/(2*a)
    else:
        print("nice try ")
elif D==0:
    print("one root")
    choice=input("do you want to find root(y/n)")
    if choice==y:
        root=-b/(2*a)
        print("root= ",root)
    else:
        print("next time")
else:
    print("no roots")

