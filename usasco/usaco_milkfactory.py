
#http://www.usaco.org/index.php?page=viewproblem2&cpid=940
#tags:tree,connected components
#difficulty : 6/10




import sys

def configure(x):
    sys.stdin=open(x+".in","r")
    sys.stdout=open(x+".out","w")

configure("factory")
n=int(input())
list1=[-1]*n
for i in range(n-1):
    a,b=map(int,input().split())
    list1[a-1]=b-1

if list1.count(-1)>1:
    print(-1)
else:
    print(list1.index(-1)+1)