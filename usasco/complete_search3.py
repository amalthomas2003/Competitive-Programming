def is_composite(num):
    for i in range(2,num):
        if num%i==0:
            return True
    else:
        return False
#######################################################################

def findlm(num):
    for i in range(num-1,1,-1):
        if num%i ==0:
            return i

for _ in range(int(input())):
    count_list=[]
    num=int(input())
    if num==1:
        print(0)
        continue
    list1=list(map(int,input().split()))
    if list1.count(list1[0])==num:
        print(0)
        continue
    bit_list=[0 for _ in range(num)]
    if is_composite(sum(list1)):
        lm=findlm(sum(list1))
        count=0
        for i in range(num):
            count_list.append(count)

            list2=[]
            count=0
            if bit_list[i]==1:
                continue
            for j in range(num):
                if bit_list[j]==1:
                    continue
                if sum(list2)+list1[j]<=lm:
                    list2.append(list1[j])
                    bit_list[j]=1
                    count+=1 if list1[j]!=lm else 0
    else:
        print(num-1)
        continue
    count_list=list(filter(lambda x:x>0,count_list))
    print(sum(count_list)-len(count_list))









