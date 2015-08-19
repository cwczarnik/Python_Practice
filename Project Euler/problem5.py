"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
#evenly divisible means no remainder
#232792560

import numpy
from numpy import *
import time
start_time = time.time()

def Euler5(step):
    list_ = xrange(11,21)
    for num in xrange(step, 10**9, step):
        for x in list_:
            if num%x!=0:
                break
        else:
            return num

print Euler5(20)
print "time " + str(time.time() - start_time ) + " seconds"
