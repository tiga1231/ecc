from ec import EllipticCurve
from util import aCurve

# EC Diffie-Hellman

x,y = 3,5
b,p = 1,7211
e = aCurve(x,y,b,p)
print e

G = e(x,y)

alice = {}
bob = {}
public = {}

#private key
alice['A'] = 12
bob['B'] = 23

print 'private:'
print alice
print bob

public['AG'] = alice['A'] * G
public['BG'] = bob['B'] * G
print 'public'
print public

alice['K'] = public['BG'] * alice['A']
bob['K'] = public['AG'] * bob['B']

print 'key exchange'
print alice
print bob
assert alice['K'] == bob['K']

