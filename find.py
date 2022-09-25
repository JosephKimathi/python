def find_min(L, i):
    min = L[i]
    index = i
    for x in range(i, len(L)):
        if L[x] < min:
            min = L[x]
            index = x
    return index         
    
