# tup1 = (1,"fhsuhd",True)
# tup2 = (2,False)
# print(tup1+tup2)
# import numpy as np 
# n1 = np.zeros((5,5))
# print(n1)
# import pandas as pd
# df = pd.DataFrame()
# list1=[1,2,3,4]
# list2=[4,5,6,7]
# df["list1"]=list1
# df["list2"]=list2
# print(df)
# dict1={"id":[1,2]}
# dict1=pd.DataFrame(dict1)
# list11=pd.DataFrame(list1)
# i=["a","b","c","d"]
# list11.index=i
# list11.loc["c"]


# def frequency_words(x):
#     li=x.split()
#     print(li)
#     d={}
#     for i in li:
#         if i not in d.keys():
#             d[i]=0
#         d[i]=d[i]+1
#     print(d)
    
# frequency_words("Hello, My name is Sayan , Sayan .")

# import math
# x=float(input("Provide a number please: "))
# print("Square root of the number is : ",math.sqrt(x).__round__(2))
# print("Square root of the number is : ",x**(1/2))

# ---------- check for a prime number----------
# x=int(input("Please enter a number that you want to check if it's a prime number or not : "))
# if (x==1):
#     print("It's not a prime number ")
# if x>1:
#     for i in range (2,x):
#         if (x%i==0):
#             print("It's not a prime number .")
#             break
#     else:
#         print("It's a prime number .")

# ---------------------- check for a armstrong number ------------------------
# inp=input("Enter a number to check if it is an armstrong number or not ? ")
# sum = 0
# size = len(inp)
# # inp = int(inp)
# for i in (inp):
#     i=int(i)
#     sum += i**size
# inp= int(inp)
# if sum == inp:
#     print("It's an armstrong number")
# else:
#     print("It's not an armstrong number")

# ------------------same for a specified interval ---------------

# for i in range(0,1000):
#     sum = 0
#     size = len(str(i))
#     for a in str(i):
#         sum += int(a)**size
#     if sum == i:
#         print(f"{i}, Armstrong number")
        
