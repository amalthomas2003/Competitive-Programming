#http://www.usaco.org/index.php?page=viewproblem2&cpid=832
#difficulty:8/10
#tags:greedy,array,dictionary


import sys
sys.stdin=open("milkorder.in","r")
sys.stdout=open("milkorder.out","w")
flag=0
n,m,k=map(int,input().split())
question_list=list(map(int,input().split()))
occupied_list=[-1]*n
taken_element_dict=dict()
for _ in range(k):
    c,p=map(int,input().split())
    occupied_list[p-1]=c
    if c==1:
        print(p)
        exit
    taken_element_dict.update({c:p-1})
if 1 in question_list:
    flag=-1
else:
    flag=1
if flag==1:
    j=0
    i=n-1
    question_list=question_list[::-1]

    while True:
        try:
            if occupied_list[i]==-1 and question_list[j] not in taken_element_dict:
                occupied_list[i]=question_list[j]
                j+=1
                i-=1
            elif occupied_list[i]!=-1:
                i-=1
            elif question_list[j] in taken_element_dict:
                i=taken_element_dict[question_list[j]]-1
                j+=1
        except:
            break
else:
    j=0
    i=0
    while True:
        try:
            if occupied_list[i]==-1 and question_list[j] not in taken_element_dict:
                occupied_list[i]=question_list[j]
                j+=1
                i+=1
            elif occupied_list[i]!=-1:
                i+=1
            elif question_list[j] in taken_element_dict:
                i=taken_element_dict[question_list[j]]+1
                j+=1
        except:
            break
if flag==-1:
    for i in range(n):
        if occupied_list[i]==1:
            print(i+1)
            exit()
else:
    for i in range(n):
        if occupied_list[i]==-1:
            print(i+1)
            exit()    


