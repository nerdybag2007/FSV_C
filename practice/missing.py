list=[1,2,3,4,5]
n=int(input("enter your number"))
for i in range(len(list)-1):
    for j in range(i+1,len(list)):
        if (list[i]+list[j]==n):
            print(i)
            print(j)

        

