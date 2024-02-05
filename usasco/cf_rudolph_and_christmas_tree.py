
#  https://codeforces.com/contest/1846/problem/D
# tags:geometry,mathematics,shapes
# good understanding of basic geometry required
# difficulty 6/10



for _ in range(int(input())):
    sum=0
    n,d,h=map(int,input().strip().split())
    list1=list(map(int,input().strip().split()))
    list1=sorted(list1,key=lambda x:x)
    for i in range(n-1):      
        sum+=(0.5)*h*d if(list1[i+1]-list1[i]>=h) else (0.5)*(list1[i+1]-list1[i])*(d+(d-((d/h)*(list1[i+1]-list1[i]))))
    print(sum+(0.5)*d*h)
    