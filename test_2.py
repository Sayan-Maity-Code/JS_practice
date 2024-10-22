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


def frequency_words(x):
    li=x.split()
    print(li)
    d={}
    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
    
frequency_words("Hello, My name is Sayan , Sayan .")