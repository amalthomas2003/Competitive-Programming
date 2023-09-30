# http://www.usaco.org/index.php?page=viewproblem2&cpid=617
# difficult: 6/10


import sys
sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

n = int(input().split()[0]) 
loc=[]
for _ in range(n):
	inp = tuple(int(i) for i in input().split())
	loc.append(inp)
ans = n

for xIndex in range(n):
	for yIndex in range(n):
		#identify the fence location vertical fence at x=xDiv; horizontal fence at y=yDiv
		xDiv = loc[xIndex][0]+1
		yDiv = loc[yIndex][1]+1
		upperLeft = 0
		upperRight = 0
		lowerLeft = 0
		lowerRight = 0
		#identify which quadrant each cows lands in
		for i in range(n):
			if loc[i][0] < xDiv and loc[i][1] < yDiv:
				lowerLeft+=1
			if loc[i][0] < xDiv and loc[i][1] > yDiv:
				upperLeft+=1
			if loc[i][0] > xDiv and loc[i][1] < yDiv:
				lowerRight+=1
			if loc[i][0] > xDiv and loc[i][1] > yDiv:
				upperRight+=1
		#figure out which region has the most cows
		worstRegion = max(upperLeft,upperRight,lowerLeft,lowerRight)
		#determine if we have found a better pair of fences
		if worstRegion < ans:
			ans = worstRegion

#print the answer
print(ans)