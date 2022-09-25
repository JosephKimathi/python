def diamond(word):
    N = len(word)
    a=0
    b = 0
    if(N%2==0):
        a=N//2-1
        b = N//2+1
    else:
        a = N//2
        b=N//2+1 
    
    count = N//2+1 
    for i in range(len(word)//2):
        line = word[a:b]
        a-=1
        b+=1
        if(N%2 == 0):
            print("{0:>{1:}}".format(line, b-1))
        else:
            print("{0:>{1:}}".format(line, count))
            count+=1
    a+=1
    b-= 1    
    count-=1
    if(N%2 !=0):
        print("{0:>{1:}}".format(word, count+1))
        line = word[a:b]
        print("{0:>{1:}}".format(line, count))
        
    for i in range(len(word)//2):
        a+=1
        b-= 1
        line = word[a:b]    
        if(N%2 == 0):
            print("{0:>{1:}}".format(line, b))
        else:
            count-=1
            print("{0:>{1:}}".format(line, count))
            
            
