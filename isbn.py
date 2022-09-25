def isbn13_to_10(s):
    s = s[3:]
    n = len(s)
    ans = []
    sum = 0
    t= 0
    for i in range(10):
        ans.append(str(i))
    ans.append('X')
    for i in range(n):
        c = s[i]
        sum+=(10-i)*int(c)
    diff = sum%11
    t = (11 - diff)%11
    print(t)
    calc = (t + int(s[9]))%11
    return s[:9]+ ans[calc]
    
