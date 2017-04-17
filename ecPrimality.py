from ec import EllipticCurve
from util import aCurve
from random import randint

def isPrime(n, scope=1000, loops=100):
    for j in range(loops):
        x,y = randint(0,n-1), randint(0,n-1)
        try:
            e = aCurve(x,y,randint(1,n-1),n)
        except AssertionError: 
            continue
        p = e(x,y)
        for i in range(1,scope):
            try:
                p = p * i
                if p.inf:
                    break
            except ValueError as e:
                k = int( str(e).split(': ')[-1].replace('L', '') )
                return False, k
    return True, 1

if __name__ == '__main__':

    while True:
        #pick a random odd for prime test
        n = 2*randint(2**100, 2**101)-1
        print n,
        test = isPrime(n, scope=5000, loops=10)
        if test[0]:
            break
        else:
            print test[1]
    print 'is probably prime'    
