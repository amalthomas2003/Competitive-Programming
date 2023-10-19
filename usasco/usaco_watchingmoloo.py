
#http://www.usaco.org/index.php?page=viewproblem2&cpid=1301
#difficulty: 6/10
#tags:greedy

n,days=map(int,input().split())
list1=list(map(int,input().split()))
new_list=[0]*200000
#print(new_list)
new_list[0]=list1[0]
curr_num=list1[0]
iter=0
end_index=0
count=0
for i in list1[1:]:
    if i-curr_num>days:
        iter+=2
    else:
        iter+=1
    
    new_list[iter]=i
    curr_num=i
for i in range(1,len(new_list)):
    if (new_list[i-1]==new_list[i]) and new_list[i]==0:
        end_index=i
        break
new_list=new_list[:end_index-1]
input_list=new_list

result = []
temp = []

for item in input_list:
    if item == 0:
        if temp:
            result.append(temp)
        temp = []
    else:
        temp.append(item)
if temp:
    result.append(temp)
#print(result)
for i in result:
    count+=i[len(i)-1]-i[0]+days+1
print(count)