# def sum():
#     a=int(input("Enter a"))
#     b=int(input("Enter b"))
#     sum=a+b
#     print(sum)

# # ==========================================================without return tpe with arguments==========================================================
# def sum(a,b):
#     sum=a+b
#     print(sum)
#     a=int(input("Enter a"))
#     b=int(input("Enter b"))
#     sum(a,b)
# # ==========================================================with return tpe without arguments==========================================================
# def sum():
#     a=int(input("Enter a"))
#     b=int(input("Enter b"))
#     sum=a+b
#     return sum
# x=sum()
# print(x)
# # ==========================================================with return tpe with arguments=========================================================
# def sum(a,b):
#     sum=a+b
#     return sum
# a=int(input("Enter a"))
# b=int(input("Enter b"))
# x=sum(a,b)
# print(sum(a,b))
def add_num():
    a=float(input("Enter a"))
    b=float(input("Enter b"))
    sum=a+b
    return sum
h=int(input("Enter height"))
sum_parll=add_num()
a_trap=(sum_parll*h)/2
RS=add_num()
PR=2*RS
print(a_trap)
print(PR)