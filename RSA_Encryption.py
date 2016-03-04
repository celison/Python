import random

def encode(s): 
     """ Given a string, return a list of numbers (ASCII values). 
     
     >>> encode('discrete') 
     [100, 105, 115, 99, 114, 101, 116, 101] 
     >>> encode('abc') 
     [97, 98, 99]
     >>> encode('Hello') 
     [72, 101, 108, 108, 111]
     """ 

     return [ord(c) for c in list(s)] 
     
def decode(ascii): 
    """ Given a list of numeric ASCII values, return the corresponding string.

    >>> decode([97, 98, 99]) 
    'abc'
    >>> decode([100, 105, 115, 99, 114, 101, 116, 101]) 
    'discrete'
    >>> deconde([72, 101, 108, 108, 111])
    'Hello'
    """ 
 
    return "".join(chr(a) for a in ascii)
  
# 1
def encrypt(e, n, m):
    """ Given an exponent to raise to, a modulus to wrap around, and a value to
    encrypt return the encrypted value.
    
    >>> encrypt(17,377,102)
    163
    >>> encrypt(17,377,72)
    11
    >>> encrypt(25, 377, 111)
    306
    """
    return (m**e)%n

# 2
def encryptstr(e, n, s):
    """ Given e, n (the modulus), and a string, encrypt each character 
    in the string and return a list of encrypted values. 
     
    >>> encryptstr(17, 377, 'discrete') 
    [341, 287, 202, 99, 95, 69, 116, 69] 
    >>> encryptstr(17, 377, 'Monday')
    [246, 310, 132, 341, 15, 270]
    >>> encryptstr(25, 377, 'College')
    [80, 306, 264, 264, 166, 25, 166]
    """
    return [ encrypt(e, n, m) for m in encode(s) ]

# 3
def decrypt(d, n, c):
    """ Given an exponent to raise to, a modulus to wrap around, and a value to
    decrypt return the corresponding value.

    >>> decrypt(257,377,341)
    100
    >>> decrypt(257,377,181)
    103
    >>> decrypt(109,291,122)
    65
    """
    return (c**d)%n

# 4
def decryptlist(d, n, l):
    """ Given d, n, and a list of numbers, decrypt each number in the list and 
    return the corresponding string. 
     
    >>> decryptlist(257, 377, [341, 287, 202, 99, 95, 69, 116, 69]) 
    'discrete'
    >>> decryptlist(257,377, [246, 310, 132, 341, 15, 270] )
    'Monday'
    >>> decryptlist(121, 377, [80, 306, 264, 264, 166, 25, 166]
    'College'
    """ 

    return "".join( chr(decrypt(d,n,a) ) for a in l )

# 5
def gcd(a, b):
    """ Given two numbers as input, returns a single number that is the largest
    integer to divide into both of them.
    
    >>> gcd(9,6)
    3
    >>> gcd(356,31)
    1
    >>> gcd(125, 750)
    125
    """
    if b == 0: 
        return a 
    else:
        return gcd(b, a % b) 
 
def phi(p, q):
    """ Given two prime numbers, return the totient ( p - 1 ) * ( q - 1).

    >>> phi(13, 29)
    336
    >>> phi(17, 19)
    288
    >>> phi(1619, 1621)
    2621160
    """
    return (p - 1) * (q - 1) 

# 6
def liste(p,q):
    """ Given two prime numbers, return a list of all usable exponents.

    >>> liste(5, 11)
    [3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39]
    >>> liste(3, 29)
    [3, 5, 9, 11, 13, 15, 17, 19, 23, 25, 27, 29, 31, 33, 37, 39, 41, 43, 45, 47, 51, 53, 55]
    >>> liste(13, 29)
    [5, 11, 13, 17, 19, 23, 25, 29, 31, 37, 41, 43, 47, 53, 55, 59, 61, 65, 67, 71, 73, 79, 83, 85, 89, 95, 97, 101, 103, 107, 109, 113, 115, 121, 125, 127, 131, 137, 139, 143, 145, 149, 151, 155, 157, 163, 167, 169, 173, 179, 181, 185, 187, 191, 193, 197, 199, 205, 209, 211, 215, 221, 223, 227, 229, 233, 235, 239, 241, 247, 251, 253, 257, 263, 265, 269, 271, 275, 277, 281, 283, 289, 293, 295, 299, 305, 307, 311, 313, 317, 319, 323, 325, 331, 335]
    """
    return [e for e in range(2,phi(p,q)) if gcd(e,phi(p,q)) == 1]


# 7
def finde(p,q):
    """ Given two prime numbers randomly pick out a useable exponent from the list,
    unless (2 ^ 16) + 1 is in the list.

    >>> finde(5,11) in liste(5,11)
    True
    >>> finde(13,29) in liste(13,29)
    True
    >>> finde(503,509) in liste(3,29)
    65537
    """
    if (2**16 + 1) in liste(p, q):
        return 2**16 + 1
    else:
        return liste(p,q)[random.randrange(0,len(liste(p,q)))]

# 8
def egcd(a, b):
    """ Given two numbers as input, returns a tuple of the (x, y) values that solve
    ax + by = gcd(a,b).
    
    >>> egcd(9, 6)
    (1, -1)
    >>> egcd(356, 31)
    (-2, 23)
    >>> egcd(2, 23)
    (-11, 1)
    """
    if (b == 0):
        return (1, 0)
    else:
        (q, r) = divmod(a, b)
        (s, t) = egcd(b, r)
        return (t, s - q * t)

# 9 10

def findd(e,p,q):
    """ Given an encrypting exponent and the two prime numbers that generated that
    number, and return the decrypting exponent.

    >>> findd(13,5,11)
    37
    >>> findd(17,29,13)
    257
    >>> findd(25,29,13)
    121
    """
    (x, y) = egcd(e, phi(p,q))
    return x % phi(p,q)

# 11
def genkeys(p,q):
    """ Given two prime numbers, p and q, return a tuple with paired
    exponents and the modulo ( e , d , n ).

    >>> genkeys(503, 509)
    (65537, 231953, 256027)
    >>> genkeys(383,389)
    (65537, 4401, 148987)
    >>> genkeys(443, 449)
    (65537, 93441, 198907)
    """
    e = finde(p,q)
    d = findd(e,p,q)
    n = p*q
    return ( e,d,n )

import unittest

class MyTest(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode('discrete'), [100, 105, 115, 99, 114, 101, 116, 101])
        self.assertEqual(encode('abc'), [97, 98, 99])
        self.assertEqual(encode('Hello'), [72, 101, 108, 108, 111] )
    def test_decode(self):
        self.assertEqual(decode([97, 98, 99]), 'abc')
        self.assertEqual(decode([100,105,115,99,114,101,116,101]), 'discrete')
        self.assertEqual(decode([72, 101, 108, 108, 111]), 'Hello' )
    def test_encrypt(self):
        self.assertEqual(encrypt(17,377,102), 163)
        self.assertEqual(encrypt(17,377,72), 11)
        self.assertEqual(encrypt(25,377,111), 306)
    def test_encryptstr(self):
        self.assertEqual(encryptstr(17, 377, 'discrete'), [341, 287, 202, 99, 95, 69, 116, 69] )
        self.assertEqual(encryptstr(17, 377, 'Monday'), [246, 310, 132, 341, 15, 270] )
        self.assertEqual(encryptstr(25, 377, 'College'), [80, 306, 264, 264, 166, 25, 166] )
    def test_decrypt(self):
        self.assertEqual(decrypt(257,377,341), 100)
        self.assertEqual(decrypt(257,377,181), 103)
        self.assertEqual(decrypt(109,291,122), 65)
    def test_decryptlist(self):
        self.assertEqual(decryptlist(257, 377, [341, 287, 202, 99, 95, 69, 116, 69] ), 'discrete')
        self.assertEqual(decryptlist(257, 377, [246, 310, 132, 341, 15, 270] ), 'Monday')
        self.assertEqual(decryptlist(121, 377, [80, 306, 264, 264, 166, 25, 166] ), 'College')
    def test_gcd(self):
        self.assertEqual( gcd(9, 6), 3 )
        self.assertEqual( gcd(356, 31), 1 )
        self.assertEqual( gcd(125, 750), 125 )
    def test_phi(self):
       self.assertEqual( phi(13,29), 336 )
       self.assertEqual( phi(17,19), 288 )
       self.assertEqual( phi(1619, 1621), 2621160 )
    def test_liste(self):
        self.assertEqual(liste(5,11),[3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39] )
        self.assertEqual(liste(13,29),[5, 11, 13, 17, 19, 23, 25, 29, 31, 37, 41, 43, 47, 53, 55, 59, 61, 65, 67, 71, 73, 79, 83, 85, 89, 95, 97, 101, 103, 107, 109, 113, 115, 121, 125, 127, 131, 137, 139, 143, 145, 149, 151, 155, 157, 163, 167, 169, 173, 179, 181, 185, 187, 191, 193, 197, 199, 205, 209, 211, 215, 221, 223, 227, 229, 233, 235, 239, 241, 247, 251, 253, 257, 263, 265, 269, 271, 275, 277, 281, 283, 289, 293, 295, 299, 305, 307, 311, 313, 317, 319, 323, 325, 331, 335] )
        self.assertEqual(liste(3,29),[3, 5, 9, 11, 13, 15, 17, 19, 23, 25, 27, 29, 31, 33, 37, 39, 41, 43, 45, 47, 51, 53, 55] )
    def test_finde(self):
        self.assertEqual(finde(5,11) in liste(5,11), True)
        self.assertEqual(finde(13,29) in liste(13,29), True)
        self.assertEqual(finde(503,509), 65537)
    def test_egcd(self):
        self.assertEqual( egcd(9, 6), (1, -1) )
        self.assertEqual( egcd(356, 31), (-2, 23) )
        self.assertEqual( egcd(2, 23), (-11, 1) )
    def test_findd(self):
        self.assertEqual( findd(13,5,11), 37 )
        self.assertEqual( findd(17,29,13), 257 )
        self.assertEqual( findd(25,29,13), 121 )
    def test_genkeys(self):
        self.assertEqual( genkeys(503, 509), (65537, 231953, 256027) )
        self.assertEqual( genkeys(383, 389), (65537, 4401, 148987) )
        self.assertEqual( genkeys(443, 449), (65537, 93441, 198907) )

unittest.main()
