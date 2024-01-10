'''

USACO 2017 US Open Contest, Bronze
Problem 3. Modern Art

http://www.usaco.org/index.php?page=viewproblem2&cpid=737

difficulty: 7/10


USACO RATING : VERY HARD

'''

import sys
sys.stdin=open("art.in","r")
sys.stdout=open("art.out","w")



list1=[]
n=int(input())
temp_list=[]
unique_array=[]


for i in range(n):
    for j in input():
        temp_list.append(j)
        unique_array.append(j) if j not in unique_array else None
    list1.append(temp_list)
    temp_list=[]
if '0' in unique_array:
    unique_array.remove('0')

coordinate_dict={}
answer=len(unique_array)


for i in unique_array:
    left_column=n
    top_row=n
    right_column=0
    bottom_row=0
    left_found=0
    right_found=0
    top_found=0
    bottom_found=0
    for j in range(n):
        for k in range(n):
            if list1[j][k]==i:
                if k<left_column:
                    left_column=k
                if k>right_column:
                    right_column=k
                if j<top_row:
                    top_row=j
                if j>bottom_row:
                    bottom_row=j
    coordinate_dict[i]=[(top_row,left_column),(bottom_row,right_column)]

overlap_dict={}

def is_overlap(num):
    for i in coordinate_dict.keys():
        if i!=num:
            temp_overlap=[]
            for j in range(coordinate_dict[i][0][0],coordinate_dict[i][1][0]+1):
                for k in range(coordinate_dict[i][0][1],coordinate_dict[i][1][1]+1):
                    if list1[j][k]==i:
                        continue
                    else:
                        temp_overlap.append(list1[j][k])
            overlap_dict[i]=temp_overlap

for i in unique_array:
    is_overlap(i)

final_list=[]
for i in overlap_dict.keys():
    for j in overlap_dict[i]:
        if j not in final_list:
            final_list.append(j)
answer=len(unique_array)-len(final_list)
print(answer)