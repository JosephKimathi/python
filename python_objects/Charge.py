class Charge:
    def __init__(self, q, x, y):
        self.q = q
        self.x = x
        self.y = y

    def str(q1):
        ans = ''
        return '"'+str(q1.q)+' @ ('+str(q1.x)+', '+str(q1.y)+ ')"'

    def potential_at(self,x,y):
        #V = kq/r
        r = ((self.x-x)**2 + (self.y-y)**2)**0.5
        k = 8.99*(10**9)
        V = self.q*k/r
        return V 