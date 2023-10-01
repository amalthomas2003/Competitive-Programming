#https://codeforces.com/contest/863/problem/B?csrf_token=e4c1158fa7c9b70f945416f3b2232b51
#tags:complete search,sorting,simulation
#difficulty 6/10

def calculate_sum(l):
    sum1=0
    for i in range(0,len(l),2):
        sum1+=l[i+1]-l[i]
    return sum1


n=int(input())
list1=list(map(int,input().split()))
list1.sort()

main_cost=9000
for i in range(2*n-1):
    for j in range(i+1,2*n):
        list2=list1[:]
        del list2[i],list2[j-1]
        #print(list1,list2,sep="\n")
        main_cost=calculate_sum(list2) if calculate_sum(list2)<=main_cost else main_cost
        #print(main_cost)
print(main_cost)


