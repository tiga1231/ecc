from ec import *
from math import factorial
from random import randint


line = '\n' + ' ' * 30


e = EllipticCurve(5, -5, 455839)
print 'e :=', repr(e)
print e, line

p1 = e(1,1)
print 'p1 :=', repr(p1)
print p1, line

p2 = e(1,1)
print 'p2 :=', repr(p2)
print p2, line

print 'p1 + p2 =', p1 + p2, line

print 'p1 - p2 =', p1 - p2, line

for i in range(10):
    print '%d*P1 ='%i, p1 * i


# factorization test

def aCurve(x,y,b,n):
    c = (pow(y,2,n) - pow(x,3,n) - b*x ) % n
    return EllipticCurve(b,c,n)

print line
print 'factorizing n = 455839 (Ch16.3):'
print 'a value error msg will give a factor of n'
x,y = 1,1
n = 162414233
n = 455839
n = 233 * 233
for kk in range(20):
    print 'trial #'+str(kk)
    e = aCurve(x,y,randint(1,n),n)
    print e
    p = e(x,y)
    for i in range(1,100):
        p = p * i
        print '%d!*P1 ='%i, p
        if p.inf:
            break
    print '%r is probabliy prime' % n




'''==============time test=================='''
from timeit import Timer

def test():
    from random import randint
    e = EllipticCurve(4,4,2773)
    p1 = e(1,3) 
    k = randint(2**1000, 2**1001)
    print sum(int(i) for i in bin(k)[2:])
    p = k * p1

n = 100
t = Timer(test)
#print t.timeit(number = n) / n
