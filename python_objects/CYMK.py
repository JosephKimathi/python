class CMYKColour:
    def __init__(self, c,m,y,k):
        if(c <0 or c>1):
            raise ValueError('c is out of bounds')
        if(m <0 or m>1):
            raise ValueError('m is out of bounds')
        if(y <0 or y>1):
            raise ValueError('y is out of bounds')
        if(k<0 or k>1):
            raise ValueError('k is out of bounds')

        self.c = c
        self.m = m
        self.y = y
        self.k = k
        
    def __eq__(self, d):
        if(self.c!=d.c or self.m !=d.m or self.y!=d.y or self.k!=d.k):
            return False
        return True
    
    def cyan(self):
        return self.c
    def magenta(self):
        return self.m
    def yellow(self):
        return self.y
    def black(self):
        return self.k