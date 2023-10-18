#http://www.usaco.org/index.php?page=viewproblem2&cpid=1012
#difficulty: 6/10
#tags: greedy
#hint: True->Flase sequence is the only time we need to flip the cow
import sys
sys.stdin=open("breedflip.in","r");sys.stdout=open("breedflip.out","w")
n,a,b=int(input()),input(),input()
print(sum(1 if x and not y else 0 for x,y in zip([True]+[True if x==y else False for x,y in zip(a,b)],[True if x==y else False for x,y in zip(a,b)])))