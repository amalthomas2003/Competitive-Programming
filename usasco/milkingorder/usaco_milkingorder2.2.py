
#did not pass all test cases


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
if 1 in question_list:
    question_list_with_one=question_list[:]
else:
    question_list_with_one=[1]+question_list[:]
j=0
list_to_be_added=list(filter(lambda x:x in question_list_with_one and x not in taken_element_set,question_list_with_one))
#print(list_to_be_added)
for i in range(n):
    if occupied_list[i] ==-1 and j<len(list_to_be_added) :
        occupied_list[i]=list_to_be_added[j]
        j+=1
#print(occupied_list)
curr_index=occupied_list.index(1)
temp_index=curr_index+1
while True:
    #print(occupied_list)

    if(check(occupied_list,question_list)):
        print(curr_index+1)
        exit()
    elif (occupied_list[curr_index]<occupied_list[temp_index] and occupied_list[temp_index] not in taken_element_set) or occupied_list[temp_index]==-1:
        occupied_list[curr_index],occupied_list[temp_index]=occupied_list[temp_index],occupied_list[curr_index]
        curr_index=temp_index
        #print(occupied_list)
    else:
        temp_index+=1
#print(temp_index+1)
        
        



