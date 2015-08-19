import numpy
from numpy import *

"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
#25164150
def sumsquaredif(N):
    
    sumsquare = sum(k for k in range(1, N+1))**2
    squaresum= sum(n**2 for n in range(1,N+1))
    return abs(squaresum-sumsquare)


print(sumsquaredif(100))
