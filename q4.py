from ec import EllipticCurve

e = EllipticCurve(-10,21,557)
p = e(2,3)
print '189P =', 189*p
print ' 63P =', 63*p
print ' 27P =', 27*p
