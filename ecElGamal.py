from ec import EllipticCurve
from util import aCurve

alice = {}
public = {}


#bob choose private key
x,y = 4,11
b,p = 3,8831
e = aCurve(x,y,b,p)
print e
bob = {'b':3}
#bob publish public key
public['G'] = e(x,y)
public['bG'] = bob['b'] * public['G']


#alice send msg
alice['msg'] = e(5,1743)
alice['k'] = 8
public['kG'] = alice['k'] * public['G']
public['cipher'] = alice['msg'] + alice['k'] * public['bG']


#bob receive msg
bob['msg'] = public['cipher'] - bob['b'] * public['kG']


print bob['msg']
