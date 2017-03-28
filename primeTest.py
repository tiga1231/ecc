from random import randint



def isPrime(n):
    return fermatPrimeTest(n)


def fermatPrimeTest(n, count=15):
    for i in range(count):
        r = randint(1,n-1)
        if pow(r, n-1, n) != 1:
            return False
    return True


def bruteForcePrimeTest(n):
    for i in xrange(2,int(n**0.5)+1):
        if n%i==0:
            print i
            return False
    return True


