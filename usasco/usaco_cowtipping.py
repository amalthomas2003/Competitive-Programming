
#http://www.usaco.org/index.php?page=viewproblem2&cpid=689
#difficulty:6/10
#tags:greedy,matrix,bit manipultion

#i assumed 0 represented un-tipped cow and 0 represent tipped cow. so I had to flip the question to get
#the right answer. 



import sys
sys.stdin=open("cowtip.in","r")
sys.stdout=open("cowtip.out","w")

def check_if_correct(l):
    global n
    count=0
    for i in l:
        for j in i:
            if j==1:
                count+=1
    if count==n*n:
        return True
    else:
        return False
    
    
def flip(l,row,column):
    for i in range(row):
        for j in range(column):
            l[i][j]=l[i][j]^1
    return l
    



n=int(input())
list1=[]
final_count=0
for _ in range(n):
    list1.append([int(x)^1 for x in input()])    #flipping the input 
while True:
    if check_if_correct(list1):
        print(final_count)
        exit()
    for i in range(n):
        for j in range(n):
            if list1[i][j]==0:
                flip_row=i
                flip_column=j
    
    flip(list1,flip_row+1,flip_column+1)
    final_count+=1



