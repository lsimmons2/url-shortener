
from math import floor

base62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encode(id):
    base = base62
    b = 62
    r = id % b
    res = base[r]
    q = floor(id / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

def decode(code):
    b = 62
    base = base62
    limit = len(code)
    res = 0
    for i in xrange(limit):
        res = b * res + base.find(code[i])
    return res
