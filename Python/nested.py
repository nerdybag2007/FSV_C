# # n=int(input("Enter n"))
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print("*",end=" ")
# #     print(" ")
        
# n=int(input("Enter n"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print(" ")    
# n=int(input("Enter n"))
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print(" ")

# n=int(input("Enter n"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print(" ")


# n=int(input("Enter n"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==j):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print(" ")
# k=1
# n=int(input("Enter n"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k+=1
#     print(" ")

# n=int(input("Enter n"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or j==1 or j==n or i==n ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")
    
n=int(input("Enter n"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or j==1 or j==n or i==n or i==j or i+j==n+1 or i-1==j-1 or i-1==n-j or (j>i and i+j<n+1)or (j<i and i+j>n+1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
    
       