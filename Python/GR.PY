a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if(a==b==c):
    print("equilateral")
elif(a==b or b==c or c==a ):
    print("isosceles")
else:
    print("scalene")




