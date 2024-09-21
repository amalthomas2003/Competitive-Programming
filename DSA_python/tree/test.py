import heapq

list1=[1,4,2,3,7,5]
sorted_list=[]

heapq.heapify(list1)
while list1:  
    sorted_list.append(heapq.heappop(list1))
print(sorted_list)