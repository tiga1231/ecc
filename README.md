# Elliptic Curve Crptography

## Usage

### Init
```python
>>> from ec import EllipticCurve
>>> e = EllipticCurve(4,4,5)

>>> print e
y^2 = x^3 + 4x + 4 mod 5

>>> p1 = e(1,2)
>>> print p1
(1,2)

>>> p2 = e(0,2)
```

### Object Reconstruction
```python
>>> print repr(e)
EllipticCurve(4,4,5)

>>> print repr(p1) 
#Point is a utility class
#use e(x,y) for constructing a point (x,y) on curve e
Point(1,2,4,4,5)
```

### Addition
```python
>>> print p1+p2
(4,3)
```

### Negation
```python
>>> print -p1
(1,3)
```


### Scalar multiplication
```python
>>> print 3*p1
(2,0)
>>> print 4*p1
Inf
>>> print -2*p2
(1,3)
```


### Point at infinity
```python
>>> p0 = e('inf')
>>> print p0
Inf
>>> print p0 + p1
(1,2)
```


### Equality
```python
>>> print p0 + p1 == p1
True
```

For more usage see test.py
