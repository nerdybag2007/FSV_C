list=[1,2,3,4,5]
n=int(input("enter your number"))
for i in range(len(list)):
    for j in range(i+1):
        if (list[i]+list[j]==n):
            print(list[i])
print(list[j])


        

