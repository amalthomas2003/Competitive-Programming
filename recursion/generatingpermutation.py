def permutation(processed,unprocessed):
    if unprocessed=="":
        print(processed)
        return
    else:
        for i in range(0,len(processed)+1):
            left=processed[0:i]
            right=processed[i:]
            permutation(left+unprocessed[0]+right,unprocessed[1:])
permutation("","1234")