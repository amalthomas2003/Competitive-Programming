import sys
sys.stdin=open("taming.in","r")
sys.stdout=open("taming.out","w")
n=int(input())
list1=list(map(int,input().strip().split()))
for i,j in enumerate(list1):   
    if j-i>0:        
        print(-1)
        exit()
z=0
curr_max=101
for i in list1:

    if i==-1:
        z+=1
    elif i<=z :
        z=0
        curr_max=i
    elif i==z+curr_max+1:
        z=0
        curr_max=i

    else:
        #print(i)
        print(-1)
        exit()
new_list=[False]*100
for i in range(n):
    if list1[i]!=-1:
        new_list[i-list1[i]]=True
min=new_list.count(True) if new_list[0]==True else new_list.count(True)+1
list1=list1[::-1]
count=0
z=0
for i in list1:
    if z<=0:
        count+=1
    if i!=-1 and z<=0:
        z=i
    else:
        z-=1
print(min,count,sep=" ")




    