import numpy
from numpy import *
import time
start_time = time.time()

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return abs(a*b) / gcd(a, b)

def euler5(n):
    if (n == 1):
        return 1
    else:
        return lcm(n, euler5(n-1))

print euler5(20)

print "took " + str(time.time() - start_time ) + " seconds"
