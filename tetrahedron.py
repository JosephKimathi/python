print("This sentence will be printed everytime the program is imported")
print("Example: tetrahedron.py from Assignment 1")
 
import math
print("Now math is imported in my python program and we can use it")

def volume(a):
                             #equivalent code
    k = 6*math.pow(2, 0.5)   #k = 6*(2**0.5)
    return math.pow(a,3)/k   #(a**3)/k
