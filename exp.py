
def exponential(x):
    ans = 1
    check = 0
    i = 1
    factor = 1
    while (ans != check):
        check = ans
        factor *= x/i
        ans += factor
        i+=1
    
    return ans
