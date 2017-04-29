from ec import EllipticCurve
e = EllipticCurve(2,3,19)
print e

print '(a)', e(1,5) + e(9,3)
print '(b)', e(9,3) + e(9,3)
print '(c)', e(1,5) - e(9,3)

for i in range(100):
    p = i*e(1,5)
    if p == e(9,3):
        print '(d)', i
        break

print '(e)'
for i in range(1,100):
    p = i*e(1,5)
    print '\t%dP ='%i, p
    if p == e('inf'):
        break

