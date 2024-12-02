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
        

# demolist= [1,2,3,4,5]
# demo_str_list=["bbdefdhigh","acslow","rest,mid"]
# demo_str_list.sort()
# print(demo_str_list)
# new_concat_str=""
# for i in range(len(demo_str_list)-1,-1,-1):
#     print(demo_str_list[i])
#     new_concat_str += demo_str_list[i]
# print(new_concat_str)

# strring = "Hello I am     Sayan"
# words = strring.split(" ")
# print(words[2])

# new_string = strring[::-1]
# print(new_string)
# new_words = new_string.split()
# new_single_space = " ".join(new_words)
# print(new_single_space)

# num = 58746
# rev_num= num[::-1]
# print(rev_num)

# def commonPrefix(left, right):
#     min_length = min(len(left), len(right))
#     for i in range(min_length):
#         if left[i] != right[i]:
#             return left[:i]
#     return left[:min_length]

# def longestCommonPrefix(strs):
#     if not strs:
#         return ""
    
#     def divideAndConquer(strs, l, r):
#         if l == r:
#             return strs[l]
#         else:
#             mid = (l + r) // 2
#             lcpLeft = divideAndConquer(strs, l, mid)
#             lcpRight = divideAndConquer(strs, mid + 1, r)
#             return commonPrefix(lcpLeft, lcpRight)
    
#     return divideAndConquer(strs, 0, len(strs) - 1)

# # Example usage:
# strings = ["flower", "flow", "flight"]
# print(longestCommonPrefix(strings))  # Output: "fl"


def facwithoutmul(n):
    if n == 0:
        return 1
    ans = 1
    for i in range(1, n + 1):
        sum = 0
        for j in range(i):
            sum += ans
        ans = sum
    return ans
    
if __name__ == "__main__":
    print(facwithoutmul(5))  
