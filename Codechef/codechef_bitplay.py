for _ in range(int(input())):
    n=int(input())
    list1=[int (x) for x in list(input())]
    count=0
    #print(list1)
    for i in range(0,n-2,2):
        temp_count=count
        print(list1[i] & list1[i+1])
        if list1[i]&list1[i+1]==list1[i+2]:
            count+=1
        if list1[i]|list1[i+1]==list1[i+2]:
            count+=1
        if list1[i]^list1[i+1]==list1[i+2]:
            count+=1
        if temp_count==count:
            print(0)
            break
    print(count)
