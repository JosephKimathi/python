from exercise1 import Charge
from exercise3 import CMYKColour
from exercise4 import RGBColour

if __name__ == '__main__':
    c1 = RGBColour(0,0,0)
    c2 = RGBColour(5,5,5)
    d1 = CMYKColour(1,1,1,1)
    d2 = CMYKColour(0.5,0.5,0.5,0.6)
    p1 = c1.to_cmyk
    print(p1)
    print(c2.as_hex)

