# y^2 = x^3 + bx + c mod p

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
            return 'Inf on y^2 = x^3 + %rx + %r mod %r' \
                                    % (self.b, self.c, self.p)
        else:     
            return 'Point(%r,%r) on y^2 = x^3 + %rx + %r mod %r' \
                                    % (self.x, self.y,
                                        self.b, self.c, self.p)


    def __add__(self, p2):
        if self.inf:
            return p2
        elif p2.inf:
            return self
        else:
            assert (self.b, self.c, self.p) == (p2.b, p2.c, p2.p)
            x1,y1 = self.x, self.y
            x2,y2 = p2.x, p2.y
            b,c,p = self.b, self.c, self.p
            #TODO
            return Point(1,2,self.b, self.c, self.p)


    def __mul__(self, a):
        #TODO
        return sum((self for i in range(a)),Point(0,0,0,0,0,True))


    def __rmul__(self, a):
        #TODO
        return self * a


class EllipticCurve():
    def __init__(self,b,c,p):
        self.b = b
        self.c = c
        self.p = p
        assert 4*pow(self.b,3,self.p) + 27*pow(self.c,2,self.p) % self.p != 0, \
                '4b^3+27c^2 = 0 not allowed'


    def sqrt(self,x):
        #TODO
        import math
        return math.sqrt(x)


    def __call__(self, x, y='+'):
        if x == 'inf':
            return Point(0,0,self.b,self.c,self.p,True)
        
        if y=='+':
            y = self.sqrt( (x**3 + self.b * x + self.c) % self.p )
        elif y == '-':
            y = -self.sqrt( (x**3 + self.b * x + self.c) % self.p )
        return Point(x,y, self.b, self.c, self.p)


if __name__ == '__main__':
    e = EllipticCurve(2,1,231)

    p1 = e(1,2)
    print repr(p1)
    print p1
    print '-' * 20

    p2 = e('inf')
    print repr(p2)
    print p2

    print '-'*20
    print p1 + p2

    print '-'*20
    print 2 * p1
    

