def sort3( a, b, c):
    one = (max(max(a,b), max(a,c)))
    two = (min(max(a,b), max(min(a,b),c)))
    hold = min(min(a,b), min(a,c))
    three = min(hold, min(a,b))
    print(one)
    print(two)
    print(three)
    return three, two, one
