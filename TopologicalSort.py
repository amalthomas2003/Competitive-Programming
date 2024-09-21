from collections import defaultdict
a,b=map(int,input().split())
list1=[]
for i in range(b):
    list1.append(input().split())
graph=defaultdict(list)
for i in list1:
    c,d=map(int,i)
    graph[c].append(d)
    graph[d].append(c)



def dfs(vertex):
    global visited_node
    count=0
    stack=[]
    visited=set()
    stack.append(vertex)
    while stack:
        count+=1
        curr=stack.pop(-1)
        visited.add(curr)
        visited_node.add(curr)
        for i in graph[curr]:
            if i not in visited:
                stack.append(i)
    return count



visited=dict()
visited_node=set()
for i in range(a):
    if i not in visited and i  not in visited_node:
        visited[i]=dfs(i)


temp=0
count=0
for i in visited:
    print(visited[i])
    temp+=visited[i]
    count+=visited[i]*(a-temp)
print(count)
