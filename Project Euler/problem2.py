import numpy
from numpy import *


"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

# Answer 4613732

        
def fib(n): # return Fibonacci series up to n.
                #I am making a list of values from the fib series
    fibarray = [] # creates an array with zero elements
    a, b = 0, 1 # assigns values to a and b
    while b < n: # this indicates that what is below will loop until false.
        fibarray.append(b) # this increases the length ofthe array with new values from b
        a, b = b, a+b #here I'm incrementing b with a and changing a to b.
    return fibarray #this returns the array with values input


def evensum(array):
    sumf=0 # creating the variable sumf 
    for i in array: #looping through elements in the array
        if i%2==0: # checking each element in the array if they are even
            sumf+=i # this sums each 
    return sumf #returns the sum when the loop is completed

print(evensum(fib(4*10**6)))
