def volume(A, h, d):
    vol = (A*h)/3
    s = "{0:.{1}f}".format(vol, d)
    return s
