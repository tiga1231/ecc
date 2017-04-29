from ec import EllipticCurve
from util import aCurve
from random import randint
import sys

n = 3900353
x,y = 1,1
for kk in range(20):
    print 'trial #'+str(kk)
    e = aCurve(x,y,randint(1,n),n)
    print e
    p = e(x,y)
    for i in range(1,100):
        try:
            p = p * i
            print '%d!*P1 ='%i, p
        except ValueError as e:
            print e
            sys.exit(0)
        if p.inf:
            break
    print '%r is probabliy prime' % n
