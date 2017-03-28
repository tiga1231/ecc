from ecc import *

line = '\n' + ' ' * 30


e = EllipticCurve(4,4,5)
print 'e :=', repr(e)
print e, line

p1 = e(0,2)
print 'p1 :=', repr(p1)
print p1, line

p2 = e(0,3)
print 'p2 :=', repr(p2)
print p2, line

print 'p1 + p2 =', p1 + p2, line

print 'p1 - p2 =', p1 - p2, line

for i in range(20):
    print '%d P1 ='%i, i * p1

