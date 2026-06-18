n=int(input("enter a number"))
list1=[1,2,3,21,32,643]
found=False
pos=1
for list in list1:
    if n==list:
        found=True
        print(f"ok hai kam{pos}")
    pos+=1
if found==False:
    print("not found")

