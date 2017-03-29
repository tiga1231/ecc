# y^2 = x^3 + bx + c mod p
from eea import inv

class Point():

    def __init__(self, x, y, b, c, p, inf=False):
        self.inf = inf
        self.x, self.y = x, y
        self.b, self.c, self.p = b, c, p
        if not self.inf:
            assert (y**2) % p == (x**3 + b*x + c) % p, \
            '\nPoint not on curve:\n%s' % self


    def __repr__(self):
        if self.inf:
            return 'Point(0,0,%r,%r,%r, inf=True)' % (self.b, self.c, self.p)
        else:
            return 'Point(%r,%r,%r,%r,%r)' % (self.x, self.y, 
                                        self.b, self.c, self.p)


    def __str__(self):
        if self.inf:
            return 'Inf'
        else:
            return '(%r,%r)' % (self.x, self.y)


    def __eq__(self, p2):
        return (self.inf == p2.inf
                and self.b == p2.b and self.c == p2.c and self.p == p2.p
                and self.x == p2.x and self.y == p2.y)


    def __add__(self, p2):
        assert (self.b == p2.b
            and self.c == p2.c
            and self.p == p2.p), 'two points not on the same curve'
        if self.inf:
            return p2
        elif p2.inf:
            return self
        elif self == (-p2):
            return Point(0, 0, self.b, self.c, self.p, True)
        else:
            x1,y1 = self.x, self.y
            x2,y2 = p2.x, p2.y
            b,c,p = self.b, self.c, self.p
            if self == p2:
                m = ((3*x1**2 + b) * inv((2 * y1)%p, p)) % p
            else:
                m = ((y2-y1) * inv((x2-x1)%p, p)) % p
            x3 = ( pow(m,2,p) - x1 - x2 ) % p
            y3 = (m * (x1-x3) - y1) % p
            return Point(x3 ,y3, self.b, self.c, self.p)


    def __neg__(self):
        return Point(self.x, (-self.y) % self.p, 
                self.b, self.c, self.p, 
                self.inf)


    def __sub__(self, p2):
        return self + (-p2)    


    def __mul__(self, a):
        #take multiples of a point using seccessive doubling
        #
        if a == 0:
            return Point(0,0,self.b,self.c,self.p, True)
        elif a==1:
            return Point(self.x, self.y, self.b, self.c, self.p)
        elif a==2:
            return self + self
        else:
            a = bin(a)[2:]
            res = self
            for i in a:
                if i == '1':
                    res += self
                res += res
            return res

            #recursion doen't work for large a
            #return (self*int(a/2))*2 + self*(a%2)
            
            # this doesn't work either
            #return sum( (self for i in xrange(a)),
            #            Point(0,0,self.b,self.c,self.p,True) )

    def __rmul__(self, a):
        return self * a


class EllipticCurve():
    def __init__(self,b,c,p):
        self.b = b
        self.c = c
        self.p = p
        assert 4*pow(self.b,3,self.p) + 27*pow(self.c,2,self.p) % self.p != 0, \
                '4b^3+27c^2 = 0 not allowed'


    def __repr__(self):
        s = 'EllipticCurve(%r,%r,%r)' 
        return s % (self.b, self.c, self.p)


    def __str__(self):
        s = 'EllipticCurve y^2 = x^3 + %rx + %r mod %r' 
        return s % (self.b,self.c,self.p)


    def sqrt(self,x):
        #TODO
        import math
        return math.sqrt(x)


    def __call__(self, x, y):
        if x == 'inf':
            return Point(0,0,self.b,self.c,self.p,True)
        '''
        if y=='+':
            y = self.sqrt( (x**3 + self.b * x + self.c) % self.p )
        elif y == '-':
            y = -self.sqrt( (x**3 + self.b * x + self.c) % self.p )
        '''
        return Point(x,y, self.b, self.c, self.p)

