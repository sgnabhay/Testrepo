# print("hello world")



#    big ___________O______________________



#----------------------------O(N)________________________
# def printItem(n):
#     for i in range(n):
#         print(i)
# printItem(10)

#       Drop Constant
# def printItem(n):
#     for i in range(n):
#         print(i)
#     for j in range(n):
#         print(j)
# printItem(10)

# it runs for (N+N)times....................

# -----------------------------------O(N^2)-----------------------

#         _____________________ RECURSSION_____________________________
# def recurssionSum(n):
#     # n=4
#     if(n<1):
#         print("n is less than 1")
#     else:
#         recurssionSum(n-1)
#         print(n)
# recurssionSum(4)




#____________________________________  FACTORIAL _____________________
# def factorialN(n):
#     assert n>=0 and int(n)== n ,'the Number should be integer.'
#     if n in [0,1]:
#         return n
#     else:
#         return n * factorialN(n-1)
# print(factorialN(5))



#__________________________________________ FIbonacci_NUmber______________


# def fibonacci(n):
#     assert n >= 0 and int(n) ==n ,'n should be integer.'
#     if n in [0,1]:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(7))


#_________________________________________ SUM OF DIGITS_____________________________


# def sumOfDigits(n):
#     assert  n>= 0 and int(n) == n ,'number should be integer.'
#     if n == 0:
#         return 0
#     else:
#         return int(n%10) + sumOfDigits(n//10)


# print(sumOfDigits(5555))


    
from lib2to3.pgen2.token import NEWLINE
from pickletools import read_uint1
from unittest import TestProgram


def swaplist(newList):
    # size = len(newList)
    newList[0],newList[-1]= newList[-1],newList[0]
    return newList
newList = [12,13,16,16,27,45,66] 
print(swaplist(newList))
