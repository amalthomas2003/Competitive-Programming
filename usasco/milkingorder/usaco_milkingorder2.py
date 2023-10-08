
#did not pass all test cases
#cumbersome approach


import sys

def check(list_big,list_small):
    
    for i in range(len(list_big)):
        try:

            if list_big[i]==list_small[0]:
                list_small.pop(0)
        except:
            return True
    if len(list_small)==0:
        return True
    else:
        return False



sys.stdin=open("milkorder.in","r")
sys.stdout=open("milkorder.out","w")

n,m,k=map(int,input().split())
question_list=list(map(int,input().split()))
occupied_list=[-1]*n
taken_element_set=set()
for _ in range(k):
    c,p=map(int,input().split())
    occupied_list[p-1]=c
    if c==1:
        print(p)
        exit
    taken_element_set.add(c)
if 1 not in question_list: 
    question_list_with_one=[1]+question_list[:]
else:
    question_list_with_one=question_list[:]
#print(question_list_with_one)
flag=0
for i in range(n):
    if occupied_list[i]==-1 and question_list_with_one:
        if flag==0:
            curr_index=i
            flag=1
        while question_list_with_one[0] in taken_element_set:
            question_list_with_one.pop(0)
        occupied_list[i]=question_list_with_one.pop(0)
#print(occupied_list)
#print(curr_index+1)
curr_index=occupied_list.index(1)
for i in range(curr_index,n):
    if (occupied_list[curr_index]<=occupied_list[i] and occupied_list[i] not in taken_element_set) or occupied_list[i]==-1:
        occupied_list[curr_index],occupied_list[i]=occupied_list[i],occupied_list[curr_index]
        
        #print(occupied_list)
        if check(occupied_list,question_list):
            curr_index=i
            print(curr_index+1)
            exit()



