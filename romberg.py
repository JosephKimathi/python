import math
import numpy

#function 
def trap(f, n, a, b):
    h = (b-a)/n
    sum = 0
    #for(i = 1; i<n;i++)
    for i in range(1, n):
        sum = sum + 2*f(a+i*h)
    
    ans = (h/2)*(f(a)+sum+f(b))
    return ans

def romberg(f, a, b, tol = 1.0e-6):
    """I, n_panels = romberg(f, a, b, tol=1.0e-6)
    Return the integral from a to b of f(x), by Romberg integration,
    as well as the number of panels used."""
    I = numpy.zeros((10,10))
    ans = numpy.zeros((10,10))
    ea = 100
    n = 1
    i = 1
    I[1,1] = trap(f, n,a,b)
    x= 0
    y = 0
    
    while(ea>tol):
        n  = 2**i
        I[i+1,1] = trap(f,n,a,b)
        for k in range(2, i+2):
            j = 2+i-k
            I[j,k] = (4**(k-1) * I[j+1, k-1] - I[j,k-1])/(4**(k-1) - 1)
            x= k
            y= j
            
        ea = 100*abs((I[1,i+1] - I[2,i]) / I[1,i+1])
        et = 100*abs((1.71828 - I[1, i+1]/1.7182))
        i+= 1
    print("n: ",n)
    print(I)
    return I[y,x], 2**(i)

if __name__ == '__main__':
    func = lambda x: x**2
    a = 0
    b = 5
    ans= romberg(func,a,b)
    print(ans)