def end_time():
    start = input("Start time:")
    end = input("Duration:")
    hr1 =int(start)//100
    min1 = int(start)%100
    x = min1+end
    add = x//60
    hr2 = (hr1+add)%24
    mins = x%60
    ans = str(hr2)+str(mins)
    return ans
    
