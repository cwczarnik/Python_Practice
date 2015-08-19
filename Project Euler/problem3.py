import numpy
from numpy import *
"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


"""
so I want to find the prime factors of a number and
then I want to check which one is the largest

"""
# Answer: 6857

def prime_factors(n):
    "Returns all the prime factors of a positive integer"
    factors = [] # create an array of the factors of a number
    d = 2 #define a paramater to test the number with
    while n>1: # a loop to keep everything in line until n is not > than 1.
        while (n%d==0): # checking the modulus of a function. 
                        # if the modulus is zero then d is a factor of n.
            factors.append(d)#adds values to the array that fit the previous statement
            n = n/d #this cuts out the previous value since we found one factor we need to check for another factor
        d = d + 1 # now we increment d so that we can do the same check as before.
                        # in case n%d is \=0 then the loop breaks and we go back to the previous loop

    return factors #output the array with the factors of the 


pfs = prime_factors(600851475143)
lpf =max(pfs) # finds the largest value of an array
print lpf 
