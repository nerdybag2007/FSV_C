# try:
#     print("please enter the marks of your subjects")
#     sub1=int(input("enter the number of 1st subject"))
#     sub2=int(input("enter the number of 2nd subject"))
#     sub3=int(input("enter the number of 3rd subject"))
#     sub4=int(input("enter the number of 4th subject"))
#     sub5=int(input("enter the number of 5th subject"))
#     total=sub1+sub2+sub3+sub4+sub5
#     percentage=(total/500)*100
#     average=total/5
#     print(f"{total},{average},{percentage}")
#     if(percentage>=90 and percentage<=100):
#         print("your grade is A please proceed")
#     elif(percentage>=80 and percentage<90):
#         print("your grade is B please proceedd")
#     elif(percentage>=70 and percentage<80):
#         print("your grade is C please proceed")
#     elif(percentage>=60 and percentage<70):
#         print("your grade is D please proceed")
#     elif(percentage<60):
#         print("your grade is F please proceed with caution")
# except ValueError:
#     print("unethical")

# ======================================================================2nd question=====================================================
# acc_bal=10000
# withdrawal=acc_bal
# if (withdrawal>10000 and withdrawal<0):
#     print("invalid input please reverify")
# elif(acc_bal>0):
#     while acc_bal>0:
#         withdrawal=int(input("enter withdrawal amount please"))
#         acc_bal-=withdrawal
#         print(acc_bal)
       
# elif(withdrawal>acc_bal or withdrawal==0):
#     print("SBI ON LUNCh BREAK")
    
    # ===========================================3rd question===============================================













# =============================================4th question=============================================================
# try:
# units=int(input("enter the number of units"))
# bill = 0
    
# if units <= 100:
#         bill = units*5
#         print(bill)
# elif units <= 200:
#         bill= (100*5)+((units-100)*7)
#         print(bill)
# else:
#         bill= (100*5)+(100*7)+((units-200)*10)
#         print(bill)
# except ValueError:
# print("not efined")
# =================================================5th questions====================================

import random

number = random.randint(1, 100)


for i in range(1, 7):
    n = int(input(f"Attempt {i}/6 - Enter your guess (1-100): "))
    if number == n:
        print("Thank you, done!")
        break  
    elif number < n <= number + 10:
        print("Too high, but close!")
    elif n > number + 10:
        print("too high!")
        
        
    
    elif n < number - 10:
        print("too low")


