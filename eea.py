def eea(r0, r1):
    '''
    Extended Euclideam Algorithm
    input: 2 integers a,b
    output: gcd, s, t such that
    gcd(a,b) = sa + bt
    '''
    s = [1,0]
    t = [0,1]
    r = [r0,r1]
    while r[-1] != 0:
        q = r[-2] / r[-1]
        s.append(s[-2] - q*s[-1])
        t.append(t[-2] - q*t[-1])
        r.append(r[-2] % r[-1])
        s,t,r = s[-2:], t[-2:], r[-2:]
    return r[-2], s[-2], t[-2]


def inv(a, p):
    '''
    compute the inverse of a mod p
    '''
    r,s,t = eea(p, a)
    if r == 1:
        return t % p
    else:
        raise ValueError, '%d is not coprime with %d' % (a, p)

        
