def isPrime(p):
    if p==1 or p==0:
        return False
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
    return True


def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)


def enque(l,a):
    if len(l) < 2:
        l.append(a)
    if len(l) == 2:
        l[0],l[1] = l[1], a
    return l


def inverse(k,p):
    a,b = p,k
    n = a

    r = a%b
    if b==1:
        return 1
    if r==0:
        return -1
    p = [0,1]
    q = [a/b, b/r]
    a = a%b
    b = b%(a%b)
        
    while r != 0:
        if b==0:
            break
        #enque(p, (p[-2]-p[-1]*q[-2])%n)
        p = [p[1], (p[-2]-p[-1]*q[-2]) % n]
        #enque(q,a/b)
        q = [q[1], a/b]
        r = a%b
        a = b
        b = r
    return (p[-2]-p[-1]*q[-2])%n


def largePrime(order):
    return 213819*2**321369+1

#k = 234982374
#k1 = inverse(k,largePrime(1))
#print k1
n = 7
print 'In Z'+str(n)+':'
print 'a, a^-1'
for i in range(1,n):
    print '%2d  %2d' % (i, inverse(i,n))


