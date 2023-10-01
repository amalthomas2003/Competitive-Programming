
#http://www.usaco.org/index.php?page=viewproblem2&cpid=964
#difficulty 6/10
#tags: complete search, subsequence , sets and maps

def find_all_substrings(input_string):
    substrings = []
    curr_highest=1

    # Iterate through the input string to find substrings
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string)+1):
            substring = input_string[i:j]
            substrings.append(substring)
    for i in substrings:
        if substrings.count(i)>1 and len(i)>curr_highest:
            curr_highest=len(i)

    return curr_highest

# Example usage:
import sys
sys.stdin=open("whereami.in","r")
sys.stdout=open('whereami.out',"w")
n=int(input())
input_string=input()
all_substrings = find_all_substrings(input_string)
print(all_substrings+1 if all_substrings>1 else 1)
