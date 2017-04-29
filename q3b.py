from fractions import gcd
n = 3900353
a, B = 2, 1000
bi = a
for i in range(2,B+1):
    bi = (bi**i) % n
    g = gcd(bi-1, n)
    if g != 1:
        print g
        break
