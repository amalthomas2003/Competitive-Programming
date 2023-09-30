
#http://www.usaco.org/index.php?page=viewproblem2&cpid=1276
#difficulty : 6/10
#tags: complete search,recursion,combitions



#find all the possible combination of air conditioners 
def combiniations(p,up):
    if up=="":
        return [p]
    return combiniations(p+up[0],up[1:])+combiniations(p,up[1:])

    
n,m=map(int,input().split())
list1=[0]*100
for _ in range(n):
    s,t,c=map(int,input().split())
    for i in range(s-1,t):
        list1[i]=c
matrix1=[]   #air conditioners as a 2d array

current_cost=100000  #max cost of one a/c is 10k so for a maximum of 10 a/c cost is 100k
for _ in range(m):
    matrix1.append(list(map(int,input().split())))
for i in combiniations("","".join(map(str,range(m)))): #basically combinations("","0123") when m=4 
    list_temp=list1[:]
    cost=0
    for j in i:
        j=int(j)
        x,y=matrix1[j][0],matrix1[j][1]
        for _ in range(x-1,y):
            list_temp[_]-=matrix1[j][2] #subtract the pi value(matrix[j][2]) from the array 
        cost+=matrix1[j][3]
    if len([ temp for temp in list_temp if temp<=0 ])==100: #check if the minimum temperature reduction is achieved
                                                            #for all the cows. if achieved the array values will be 
                                                            #atmost 0
        if cost<current_cost:
            current_cost=cost
print(current_cost)        



