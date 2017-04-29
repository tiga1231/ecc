from ec import EllipticCurve
p = 593899
e = EllipticCurve(7,11,p)
for i in range(10):
    x = 123450 + i
    r = (x**3 + 7*x + 11 ) % p
    y = pow(r, (p+1)/4, p)
    if y**2 % p == r:
        print e(x,y)
