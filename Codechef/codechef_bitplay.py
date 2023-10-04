
#https://www.codechef.com/problems/BITPLAY?tab=statement
#difficulty:5/10
#tags:bitwise operators

for _ in range(int(input())):
    n=int(input())
    list1=[int (x) for x in list(input())]
    count=0
    temp_var=1
    for i in range(0,n-2,2):
        count=0
        if list1[i]&list1[i+1]==list1[i+2]:
            count+=1
        if list1[i]|list1[i+1]==list1[i+2]:
            count+=1
        if list1[i]^list1[i+1]==list1[i+2]:
            count+=1
        temp_var*=count
    print(temp_var % 1000000007 )
