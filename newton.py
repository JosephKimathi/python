def sqrt(a):
    x = a
    xn = (x+a/x)/2
    eps = 10e-15
    while (abs(xn - x) >= eps):
        x = xn
        xn = (x+a/x)/2
        
    return xn
     
