
import heapq


graph=[
    [0,5,8,float('inf')],
    [5,0,9,2],
    [8,9,0,6],
    [float('inf'),2,6,0]
]

#graph with negative cycles
graph1=[
    [0,float('inf'),6,-6,float('inf')],
    [3,0,float('inf'),float('inf'),float('inf')],
    [float('inf'),float('inf'),0,1,float('inf')],
    [float('inf'),1,float('inf'),0,float('inf')],
    [float('inf'),float('inf'),float('inf'),float('inf'),0]
]

graph = [
    [0, 3, float('inf'), 7, 8],  # A
    [3, 0, 4, 2, float('inf')],  # B
    [float('inf'), 4, 0, 5, 6],  # C
    [7, 2, 5, 0, 1],             # D
    [8, float('inf'), 6, 1, 0]   # E
]



def disjkstra(node):
    global graph
    visited=set()
    heap=[]
    heapq.heappush(heap,(0,node))
    min_distance=[float('inf')]*len(graph)
    min_distance[node]=0
    prev_nodes=[None]*len(graph)
    while heap:
        dist,curr_node=heapq.heappop(heap)
        visited.add(curr_node)
        for index,to_node_distance in enumerate(graph[curr_node]):
            if index in visited:
                continue
            else:
                if min_distance[index]>dist+to_node_distance:
                    min_distance[index]=dist+to_node_distance
                    prev_nodes[index]=curr_node
            heapq.heappush(heap,(min_distance[index],index))
    print(min_distance)
    def printresult(prev_nodes,node,string):
        if node==None:
            return string
        string+=str(node)
        return printresult(prev_nodes,prev_nodes[node],string)
        
        


    for i in range(len(prev_nodes)):
        print("->".join(list(printresult(prev_nodes,i,"")[::-1])))




disjkstra(0)
