
def neville(x_data, y_data, x):
    """p = neville(x_data, y_data, x)
    Evaluate the polynomial interpolant p(x) that passes through the
    specified data points by Neville's method."""
    n = len(x_data)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k==0:
                p[i]=(y_data[i])
            else:
                p[i] = ((x-x_data[i+k])*p[i]+ (x_data[i]-x)*p[i+1])/ (x_data[i]-x_data[i+k])    

    return p[0]

xdata = [2,4,6]
ydata = [5,6,8]
print(neville(xdata,ydata,4.5))