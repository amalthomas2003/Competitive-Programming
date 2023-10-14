# http://www.usaco.org/index.php?page=viewproblem2&cpid=892
#difficulty 7/10
#tags : adhoc,array




def issorted(l,n,start,end):
    if l[start:end]==[i+1 for i in range(n)]:

        return True
    else:

        return False


import sys
sys.stdin=open("sleepy.in","r")
sys.stdout=open("sleepy.out","w")

n=int(input())
list1=list(map(int,input().strip().split()))
new_list=[0]*300
for _ in range(n):
    new_list[_]=list1[_]
start_index=0
end_index=n-1
count=0
for i in range(n):
    if issorted(new_list,n,start_index,end_index+1):
        print(count)
        exit()

    else:
        count+=1
        temp_first=new_list[start_index]
        new_list[start_index]=0
        curr_max=new_list[end_index]+1
        swap_index=end_index+1

        for j in range(n):
            if new_list[end_index-j]>temp_first and new_list[end_index-j]<curr_max:
                curr_max=new_list[end_index-j]
                swap_index=end_index-j
                

            else:
                break
        end_index+=1
        start_index+=1
        new_list=new_list[:swap_index]+[temp_first]+new_list[swap_index:]
        
        


