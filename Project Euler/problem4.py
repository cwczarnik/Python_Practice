import numpy
from numpy import *

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two distinct 3-digit numbers.
"""

#Answer: 906609

# handy function to check if a number is palindrome
def palcheck(i):
    return str(i) == str(i)[::-1]

# what's the max?
#I'll make a function

# multiply all numbers `i` between 100 and 998, with all between i+1 and 999
def maxpal():
    maxprod=0;
    a,b=0,0
    #all numbers from 
    for a in xrange(100,998):
        for b in xrange(a+1,1000):
            prod = a*b
            #setting a conditional to control the value of the product
            if palcheck(prod) and (prod > maxprod):
                maxprod = prod
    return maxprod

print(maxpal())
