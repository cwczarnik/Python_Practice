import numpy
from numpy import *

a = []
for i in range(1,6):
    print(i)
    a.append(i)
print(a)
a.append("hello")
print(a)

##
##def fib(n):
##    fibarray = [] 
##    a, b = 0, 1 
##    while b < n: 
##        fibarray.append(b)
##        a, b = b, a+b
##    print fibarray
