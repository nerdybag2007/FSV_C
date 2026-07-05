op=input("enter the operation")

match op:
    case "s":
        s=int(input("enter the side of square"))
        print("area of rectangle",s*s)
    case "r":
        r1=int(input("enter the side1 of rectangle"))
        r2=int(input("enter the side2 of rectangle"))
        print("rectangle's area",r1*r2)
    case "c":
        r=float(input("enter raidus"))
        print("area of circle",(3.14*r*r))
    case "t":
        b=float(input("enter base"))
        h=float(input("enter hieght"))
        print("area of triangle",(0.5)*b*h)
    case _:
        print("invalid")
 
            

