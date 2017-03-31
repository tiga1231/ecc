from ec import EllipticCurve

def aCurve(x,y,b,n):
    c = (pow(y,2,n) - pow(x,3,n) - b*x ) % n
    return EllipticCurve(b,c,n)
