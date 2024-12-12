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


# def facwithoutmul(n):
#     if n == 0:
#         return 1
#     ans = 1
#     for i in range(1, n + 1):
#         sum = 0
#         for j in range(i):
#             sum += ans
#         ans = sum
#     return ans
    
# if __name__ == "__main__":
#     print(facwithoutmul(5))  


# printing star as an assignment
# n= int(input())
# n=5
# mid = n//2
# # print(mid)
# for i in range(n):
#     if i <= mid:
#         print("-"*(mid-n),end=" "),print("*",end=" "),print("-"*(mid-n),end =" ")
        
# ------- still to understand--------

# name_grade_list=[]
# while True:
#     name = input("Please enter the name of the candidate: ")
#     if name.lower() == "done":
#         break
    
#     try:
#         grade = float(input("Please enter the grade of the student: "))
#     except:
#         print("Please enter a float value")
#         continue
        
#     college="SVIST"
# #     name_grade_list.append([name,grade,college])
# # print(name_grade_list)
# # print(len(name_grade_list))
# # acc_grade=0
# # for student in name_grade_list:
# #     print(student[1])
# #     acc_grade+=student[1]
# # avg = acc_grade/len(name_grade_list) if name_grade_list else 0
# # print("Average",avg)
# # ------------------------ with the help of dictenory-----------------
#     name_grade_list.append({"name":name,"grade":grade,"college":college})

# sorted_list=[]

# for i in name_grade_list:
#     print(i["grade"])
#     sorted_list.append(i["grade"])

# sorted_list=sorted(name_grade_list,key=lambda x : x["grade"],reverse=True)
# print(sorted_list)
# for i in sorted_list:
#     print(f"name is {i["name"]} grade is {i["grade"]}")
# ------------------------Pairs divisible by 2--------------------
# def divisibleByTwo(x):
#     emp_list=[]
#     start=0
#     while start < len(x):
#         for i in (x):
#             emp_list.append((x[start],i))
#         start+=1
#     # print(emp_list)
#     final_list=[]
#     for i in emp_list:
#         if (i[0]+i[1]) % 2 == 0:
#             final_list.append(i)
#     return (f"The final pairs that are devided by 2 are \n {final_list} \n and it's length is \n {len(final_list)}")

# print(divisibleByTwo([1,2,4,6,8,7]))

# --------------------------------------------------

# def checkNUmberOfOccurances(s1,s2):
#     occurance = 0
#     for c in s2:
#         occurance += s1.count(c)
#     return occurance 

# print(checkNUmberOfOccurances("developer","dev"))
# -----------------------------------------
# def unionOfTwoSortedArray(arr1,arr2):
#     merged_list=arr1+arr2
#     #arr1.sort()#updates the original list
#     #return(set(arr1))
    
#     unique_sorted_list= list(set(merged_list))
#     final_list=sorted(sorted(unique_sorted_list))#return a new list for sorted
#     return final_list
# print(unionOfTwoSortedArray([1,2,3,4],[-2,3,5,7]))

# ----------------------------------
# def printGoodNumberorBadNumber(num):
#     total=0
#     original_num = num
#     while num > 0:
#         temp = num % 10
#         total+=temp
#         num = num//10
#     if original_num % total == 0:
#         return ("Good Number")
#     else:
#         return ("Bad Number")

# print(printGoodNumberorBadNumber(int(input("Enter a digit: "))))

# ------------------------------------------------------------
# def findLargestSmallest(x):
#     x=int(x)
#     num=[]
#     start=0
#     while x > 0:
#         temp = x % 10
#         num.append(temp)
#         x = x//10
#     for i in range (0,len(num)):
#         for j in range (i+1,len(num)):
#             if num[i]<=num[j]:
#                 num[i],num[j]=num[j],num[i]
#     return [num[0],num[len(num)-1]]

# print(findLargestSmallest("3287"))
# -------------------------------------------------------------

# def findLastOccurance(num,x):
#     final_list=[]
#     n=len(final_list)-1
#     for index,value in enumerate(num):
#         if value == x:
#             final_list.append([value,index])
#     first_index=final_list[0][1]
#     last_index=final_list[n][n]
#     return {first_index,last_index}

# print(findLastOccurance("organization","o"))
# ---------------------------------------------
# def uncommonCharacter(s1,s2):
#     s1=s1.strip()
#     s2=s2.strip()
#     emp_list=[]
#     count = 0
#     for c in s1:
#         if c not in s2:
#             emp_list.append(c)
#     for ch in s2:
#         if ch not in s1:
#             emp_list.append(ch)
#     print(emp_list)
#     return "".join(list(set(emp_list)))

# print(uncommonCharacter("digital","ninja "))

# -----------------------------------------------------------
# def twoWheelerFourWheeler(v,w):
#     bike = ((v*4)-w)/2
#     car = v-bike
#     print(f"The number of two wheelers are {bike} and the number of four wheelers are {car}")
    
# print(twoWheelerFourWheeler(200,540))
# ======================================================
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         i = 0
#         j=0
#         flag = 0
#         while i < len(s):
#             for i in range(len(s)):
#                 if s[i] not in t:
#                     return False
#             i+=1
#             flag = 1
#         while j<len(t):
#             for ch in t :
#                 if ch not in s and flag == 1:
#                     return False
#             j+=1
#         return True    
# #still not optimized
# from collections import Counter
# s1 = "sayan"
# s2="Maity"
# s1_count=Counter(s1)
# s2_count=Counter(s2)
# print(s1_count,type(s2_count))
# print(s1_count["S".lower()])
            
# =====================================================================
# def removeVowelsString(s):
#     vowel_list=["a","e","i","o","u"]
#     for vow in vowel_list:
#         s=s.replace(vow,"")
#     return s

# print(removeVowelsString("welcome to tcs digital"))
# ============================================================

# import math
# def calculateAreaCircle(d):
#     r=int(d)/2
#     return (math.pi*r**2)
# print(calculateAreaCircle(3))
# ============================================================
# def findFactorial(x):
#     if x == 0 or x==1:
#         return 1
#     else:
#         return x*findFactorial(x-1)



# def relatedByBlood(p):
#     emp_list=[]
#     total=0
#     p=int(p)
#     original_p = p
#     while p > 0 :
#         n=p%10
#         emp_list.append(n)
#         p=p//10
#     for c in emp_list:
#         total+=findFactorial(c)
#     if total==original_p:
#         return 1
#     else:
#         return 0

# print(relatedByBlood(14))

# ==================================================
# def checkSubstring(s1,s2):
#     l=len(s2)
#     for i in range(len(s1)-l):
#         if s2 == s1[i:i+l]:
#             print(f"Index is {i+1}")
#             return True
#     return False

# print(checkSubstring("abcjhafsj","fah"))

# =====================================================
# def findEmptyPacketandPush(arr):
#     count = 0
#     result=[]
#     for c in arr:
#         if c == 0:
#             count+=1
#         else:
#             result.append(c)
#     print(count)
#     result.append([0]*count) #[1, 2, 6, 7, 9, 8, 4, [0, 0]]
#     result.extend([0]*count) #[1, 2, 6, 7, 9, 8, 4, 0, 0]
#     return result
# print(findEmptyPacketandPush([1,2,6,7,9,0,8,0,4]))

# =================================================================
# def findLongestCommonPrefix(arr):
#     if not arr:
#         return ""
#     prefix = arr[0]
#     print(prefix)
#     for strings in arr[1:]:
#         while strings[:len(prefix)] != prefix and prefix:
#             prefix = prefix[:len(prefix)-1]
#         if not prefix:
#             break
#     return prefix
                
          
# print(findLongestCommonPrefix(["flower",'flow',"flight"]))

# ===============================================================================
# def calculateProductPrice(x):
#     x = int(x)
#     res = 1
#     while x>0:
#         rem = x%10
#         res*=rem
#         x=x //10
#     return res
# print(calculateProductPrice(input("Enter the price: ")))
# =============================================================

        
# arr = [12,6,4,7,8]
# for index,value in enumerate(arr):
#     print(f"index is {index} and value is {value}")

# def findArmstrong(x):
#     len_x=len(str(x))
#     x= int(x)
#     total = 0
#     org_num = x
#     while x>0:
#         rem = x%10
#         total += rem**len_x
#         x = x//10
        
#     if org_num == total:
#         return("Armstrong Number")
#     else:
#         return("Not an armstrong number")
# print(findArmstrong(1534))

# ========================================
# def checkEvenorOdd(x):
#     if x% 2 == 0:
#         return ("even")
#     else:
#         return("Odd")
# print(checkEvenorOdd(-12))

# def checkHarshadNumber(x):
#     total = 0
#     real_number = x
#     while x>0:
#         rem = x%10
#         total+=rem
#         x = x//10
#     if real_number % total == 0:
#         return ("Harshad Number")
#     else:
#         return ("Not a harshad number")
# print(checkHarshadNumber(int(input("enter a number: "))))

# def checkPalindrome(x):
#     real_number = x
#     total=0
#     while x>0:
#         rem = x%10
#         total = total*10+rem
#         x = x//10
#     print(total)
#     if total == real_number:
#         return ("Palindrome")
#     else:
#         return("Not a Palindrome")
# print(checkPalindrome(123))
        
# def chocolatePackingProblem(x):
#     choc_list=[]
#     count=0
#     for i in range(x):
#         choc_list.append(int(input("Enter an integer value: ")))
#     i=0
#     while i < len(choc_list):
#         if choc_list[i]==0:
#             choc_list.pop(i)
#             count+=1
#         i+=1
#     choc_list.extend([0]*count)
#     return choc_list

# print(chocolatePackingProblem(4))

# ac=[1,2,3]
# # for i in range(len(ac)):
# #     ac.replace(ac[i],[8])
# for i in range(3):
#     ac.insert(0,6)
# print(ac)
#valuable knowledge insert,pop is best for list, extends works at end