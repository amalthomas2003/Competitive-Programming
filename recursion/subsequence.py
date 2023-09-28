def permutation(processed,unprocessed):
    if unprocessed=="":
        return [processed]
    left=permutation(processed+unprocessed[0],unprocessed[1:])
    right=permutation(processed,unprocessed[1:])
    left+=right
    return left
print(permutation("","123"))
    