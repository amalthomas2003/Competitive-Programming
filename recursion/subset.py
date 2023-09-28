def subset(processed,unprocessed):
    if len(unprocessed)==0:
        global main_list
        main_list.append(processed)
        #alternativey just use print statement and return to just display the subsets
    else:
        subset(processed+unprocessed[0],unprocessed[1:])
        subset(processed,unprocessed[1:])
main_list=[]
subset("","123")
print(main_list)

