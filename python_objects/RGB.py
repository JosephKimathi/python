

class RGBColour:
    def __init__(self, r,g,b):
        if(r<0 or r>255):
            raise ValueError('r is out of bounds')
        if(g<0 or g>255):
            raise ValueError('g is out of bounds')
        if(b <0 or b>255):
            raise ValueError('b is out of bounds')

        self.r = r
        self.g = g
        self.b = b

    def red(self):
        return self.r

    def green(self):
        return self.g

    def blue(self):
        return self.b

    def luminance(self):
        return 0.299*self.r + 0.587*self.g + 0.114*self.b

    def __eq__(self, c):
        if(self.r!= c.r or self.g != c.g or self.b != c.b):
            return False
        return True