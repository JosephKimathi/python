import math

def polar_to_cartesian(r, t, d):
    theta = math.radians(t)
    y = r*math.sin(theta)
    x = r*math.cos(theta)
    return('({0:.{1}f}, {2:.{1}f})'.format(x, d, y))    
