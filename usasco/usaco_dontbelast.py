
#USACO 2017 January Contest, Bronze
#Problem 1. Don't Be Last!

#http://www.usaco.org/index.php?page=viewproblem2&cpid=687

#difficuly:5/10

#tags:dictionary,maps,collections


import sys
from collections import defaultdict
sys.stdin=open("notlast.in","r")
sys.stdout=open("notlast.out","w")
cow_name_dict=defaultdict(int)
cow_name_dict["Bessie"]=0
cow_name_dict["Elsie"]=0
cow_name_dict["Daisy"]=0
cow_name_dict["Gertie"]=0
cow_name_dict["Annabelle"]=0
cow_name_dict["Maggie"]=0
cow_name_dict["Henrietta"]=0
set1=set()
for _ in range(int(input())):
    a,b=map(str,input().split())
    cow_name_dict[a]+=int(b)
for i in cow_name_dict.values():
    set1.add(i)
if len(set1)==1:
    print("Tie")
    exit()
else:
    list1=list(set1)
    set1.remove(min(list1))
    list1=list(set1)
    value_to_remove=min(list1)
count_of_value_to_remove_in_cow_name_dict=0
for i in cow_name_dict.values():
    if i == value_to_remove:
        count_of_value_to_remove_in_cow_name_dict+=1
if count_of_value_to_remove_in_cow_name_dict>1:
    print("Tie")
    exit()
else:
    for i,j in cow_name_dict.items():
        if j==value_to_remove:
            print(i)
            exit()
        
    
    
    