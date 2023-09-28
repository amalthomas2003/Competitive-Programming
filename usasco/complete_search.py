#  http://www.usaco.org/index.php?page=viewproblem2&cpid=712
import sys
sys.stdin=open("circlecross.in","r")
sys.stdout=open("circlecross.out","w")
string=input()
count=0
for i in range(len(string)):
    lindex=string.find(string[i])
    rindex=string.rfind(string[i])
    new_str=string[lindex+1:rindex]
    for j in new_str:
        if new_str.count(j)>1:
            continue
        else:
            count+=1
print(count//4)
            
