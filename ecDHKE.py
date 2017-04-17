from ec import EllipticCurve
from util import aCurve

# EC Diffie-Hellman Key Exchange

alice = {}
bob = {}
public = {}

x,y = 3,5
b,p = 1,7211
e = aCurve(x,y,b,p)
G = e(x,y)
#public info
public['e'] = e
public['G'] = G

print 'public setup'
print public

#private key
alice['A'] = 12
bob['B'] = 23

print 'private setup'
print 'alice:', alice
print 'bob:', bob

#alice publish her K_pub
public['AG'] = alice['A'] * public['G']
#bob
public['BG'] = bob['B'] * public['G']

print 'public channel'
print public

#alice bob get their shared key
alice['K'] = public['BG'] * alice['A']
bob['K'] = public['AG'] * bob['B']

print 'after key exchange'
print alice
print bob
assert alice['K'] == bob['K']

